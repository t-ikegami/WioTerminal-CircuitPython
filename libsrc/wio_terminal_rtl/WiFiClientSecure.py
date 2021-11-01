from micropython import const
import time
from .rpc import ssl
from .rpc import constants as C
from .WiFiClient import WiFiClient

_MAX_WRITE_RETRY      = const(10)

class WiFiClientSecure (WiFiClient) :
    
    def __init__(self, fd = None) :
        self.fd = fd
        self.rootCA     = None
        self.cliCert    = None
        self.cliKey     = None
        self.pskIdent   = None
        self.psKey      = None
        self.timeout    = 30_000	# in msec
        self.sslclient  = None
        self.rxbuf      = None
        self.conn_staus = 0
        
    def __del__(self) :
        self.stop()

    def connect(self, host, port, timeout = None, rootCA = None, cliCert = None, cliKey = None,
                pskIdent = None, psKey = None) :
        if isinstance(host, tuple) : host = ".".join(str(x) for x in host)

        if timeout  is not None : self.timeout  = timeout
        if rootCA   is not None : self.rootCA   = rootCA  
        if cliCert  is not None : self.cliCert  = cliCert 
        if cliKey   is not None : self.cliKey   = cliKey  
        if pskIdent is not None : self.pskIdent = pskIdent
        if psKey    is not None : self.psKey    = psKey   

        if self.sslclient is None :
            self.sslclient = ssl.client_create()
            if self.sslclient == 0 :	# NULL
                self.sslclient = None
                raise RuntimeError("Could not ssl.client_create")
            ssl.init(self.sslclient)

        if self.timeout > 0          : ssl.set_timeout (self.sslclient, self.timeout )
        if self.rootCA   is not None : ssl.set_rootCA  (self.sslclient, self.rootCA  )
        if self.cliCert  is not None : ssl.set_cliCert (self.sslclient, self.cliCert )
        if self.cliKey   is not None : ssl.set_cliKey  (self.sslclient, self.cliKey  )
        if self.pskIdent is not None : ssl.set_pskIdent(self.sslclient, self.pskIdent)
        if self.psKey    is not None : ssl.set_psKey   (self.sslclient, self.psKey   )

        ret = ssl.start_client(self.sslclient, host, port, self.timeout)
        if ret < 0 :
            self.stop()
            raise RuntimeError("Could not ssl.start_client: " + hex(-ret))

        self.fd = ssl.get_socket(self.sslclient)
        self.conn_staus = time.monotonic_ns()
        
        return 1

    def write(self, data) :
        if self.fd is None : return 0

        if isinstance(data, int) :
            mv = memoryview(bytes([data]))
        else :
            mv = memoryview(data)

        totalBytesSent = 0
        retry = _MAX_WRITE_RETRY
        while len(mv) > 0 :
            retry -= 1
            if retry <= 0 : break

            res = ssl.send_data(self.sslclient, mv, len(mv))
            if res > 0 :
                totalBytesSent += res
                mv = mv[res:]
                retry = _MAX_WRITE_RETRY
            elif res not in (0, C.MBEDTLS_ERR_SSL_WANT_WRITE, C.MBEDTLS_ERR_SSL_WANT_READ) :
                self.stop()
                raise RuntimeError("Could not ssl.send_data: " + hex(-res))
            
        return totalBytesSent
    
    def _read(self, max = 1024) :
        # get_receive() may return -76 when underlying socket is not
        # ready.  Calling available() seems to alleviate the symptom.
        # Even if available(), get_receive() may fail when the
        # connection is about to be closed.  Subsequent call of
        # available() and get_receive() return False and 0,
        # respectively.
        # 
        if not self._available() : return None
        (buf, res) = ssl.get_receive(self.sslclient, max)
        if res <= 0 :
            if res in (0, C.MBEDTLS_ERR_SSL_WANT_READ, C.MBEDTLS_ERR_SSL_WANT_WRITE) : return None
            self.stop()
            if res not in (C.MBEDTLS_ERR_SSL_PEER_CLOSE_NOTIFY, C.MBEDTLS_ERR_NET_CONN_RESET) :
                raise RuntimeError("Could not ssl.get_receive: " + hex(-res))
            return None
        return buf

    def stop(self) :
        if self.sslclient is None : return
        ssl.stop_socket(self.sslclient)
        ssl.client_destroy(self.sslclient)
        self.sslclient = None
        self.fd = None

    def verify(self, fp, domain_name) :
        if self.sslclient is None : return False
        return ssl.verify_fingerprint(self.sslclient, fp, domain_name)
