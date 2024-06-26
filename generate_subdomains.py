from generate_lists import generate_lists

def wildcard_subdomains():
    """
    Creates lists to be used in a firewall. Specifically:
    1. Creates a new list of domains with a wildcard subdomain
    2. Deduplicates output so only unique lines remain
    3. Appends wildcard subdomain list to the list of tlds
    """
    final_tlds = generate_lists()
    wildcard_subdomains = [f'\*\.{i}' for i in final_tlds]
    wildcard_subdomains.sort()
    print(wildcard_subdomains)

    with open("lists/tlds.txt", "w") as f:
        f.write("\n".join(wildcard_subdomains))
    print(f'> DONE. List of subdomains generated. It contains {len(wildcard_subdomains)} subdomains.')

if __name__ == '__main__':
    wildcard_subdomains()
