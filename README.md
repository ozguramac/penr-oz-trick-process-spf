Trick
---------

Extract IP and domain list from SPF records

    wepay.com: 
      v=spf1 a mx include:_spf.google.com include:sendgrid.net ip4:216.58.192.0/19 ip6:2607:f8b0:4000::/36 -all
    _spf.google.com: 
      v=spf1 ip4:216.58.192.0/19 include:_netblocks.google.com include:_netblocks2.google.com include _netblocks3.google.com ~all
    _netblocks.google.com:
      v=spf1 ip4:64.18.0.0/20 ip4:64.233.160.0/19 ip4:66.102.0.0/20 ip4:66.249.80.0/20 ip4:72.14.192.0/18 ip4:74.125.0.0/16 ip4:108.177.8.0/21 ip4:173.194.0.0/16 ip4:207.126.144.0/20 ip4:209.85.128.0/17 ip4:216.58.192.0/19 ip4:216.239.32.0/19 ~all
    _netblocks2.google.com':
      v=spf1 ip6:2001:4860:4000::/36 ip6:2404:6800:4000::/36 ip6:2607:f8b0:4000::/36 ip6:2800:3f0:4000::/36 ip6:2a00:1450:4000::/36 ip6:2c0f:fb50:4000::/36 ~all
      
 becomes
    
    ['wepay.com', '_spf.google.com', 'sendgrid.net', '_netblocks.google.com', '_netblocks2.google.com', '_netblocks3.google.com']
    ['216.58.192.0/19', '2607:f8b0:4000::/36', '64.18.0.0/20', '64.233.160.0/19', '66.102.0.0/20', '66.249.80.0/20', '72.14.192.0/18', '74.125.0.0/16', '108.177.8.0/21', '173.194.0.0/16', '207.126.144.0/20', '209.85.128.0/17', '216.239.32.0/19', '2001:4860:4000::/36', '2404:6800:4000::/36', '2800:3f0:4000::/36', '2a00:1450:4000::/36', '2c0f:fb50:4000::/36']
