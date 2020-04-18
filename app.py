def spf(domain):
    if domain == 'wepay.com':
        return "v=spf1 a mx include:_spf.google.com include:sendgrid.net ip4:216.58.192.0/19 ip6:2607:f8b0:4000::/36 -all"
    if domain == '_spf.google.com':
        return "v=spf1 ip4:216.58.192.0/19 include:_netblocks.google.com include:_netblocks2.google.com include:_netblocks3.google.com ~all"
    if domain == '_netblocks.google.com':
        return "v=spf1 ip4:64.18.0.0/20 ip4:64.233.160.0/19 ip4:66.102.0.0/20 ip4:66.249.80.0/20 ip4:72.14.192.0/18 ip4:74.125.0.0/16 ip4:108.177.8.0/21 ip4:173.194.0.0/16 ip4:207.126.144.0/20 ip4:209.85.128.0/17 ip4:216.58.192.0/19 ip4:216.239.32.0/19 ~all"
    if domain == '_netblocks2.google.com':
        return "v=spf1 ip6:2001:4860:4000::/36 ip6:2404:6800:4000::/36 ip6:2607:f8b0:4000::/36 ip6:2800:3f0:4000::/36 ip6:2a00:1450:4000::/36 ip6:2c0f:fb50:4000::/36 ~all"
    return None


def extract_ip_list(domain, domain_set, address_set):
    spf_rec = spf(domain)
    if not spf_rec:
        return

    tokens = spf_rec.split(' ')

    include_tokens = [t for t in tokens if t.startswith('include')]
    domains = [d.split(":")[-1] for d in include_tokens]
    domain_set.extend([d for d in domains if d not in domain_set])

    ip_tokens = [t for t in tokens if t.startswith('ip')]
    addresses = [a.split(":", 1)[-1] for a in ip_tokens]
    address_set.extend([a for a in addresses if a not in address_set])

    for d in domains:
        extract_ip_list(d, domain_set, address_set)


all_domains = ['wepay.com']
all_addresses = []
extract_ip_list('wepay.com', all_domains, all_addresses)

print(all_domains)
print(all_addresses)
