import jenkins.model.*

def instance = Jenkins.getInstance()

final String name = "127.0.0.1"
final int port = 9001
final String userName = ""
final String password = ""
final String noProxyHost = ""

final def pc = new hudson.ProxyConfiguration(name, port, userName, password, noProxyHost)
instance.proxy = pc
instance.save()
println "Proxy settings updated!"