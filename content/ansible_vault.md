Title: Encrypting secrets with Ansible Vault
Date: 2020-01-22 09:12
Category: Ansible
Tags: ansible
Authors: Eric Rochow
Summary: Protect secrets with ansible-vault

### Configure config file to understand identities

Add the following under the `[defaults]` heading of either `~/.ansible.cfg` or `/etc/ansible/ansible.cfg`:
```
[defaults]
vault_identity_list = $vault_id1@/path/to/$vault_id1_key,$vault_id2@/path/to/$vault_id2_key,...$vault_idn@/path/to/vault_idn_key
```

### Create vault ID
Now it's time to create the actual vault file. This can be done by either copy-and-pasting a password into the file specified in the config file or by randomly generating one with the tool of your choice and redirecting into a file.
```
echo "$(openssl rand -hex 32)" > /path/to/$vault_id1_key
```

### Use the vault ID

Now rather than being prompted for a password, it is possible to apply a label to the vault. The label can then look up the password from the vault key file.
```
ansible-vault create --encrypt-vault-id $vault_id1 vault.yml
```
### Example

As an example of the above, let's create a vault named `prod_secrets.yml` with the label `prod` with the password stored in a key file named `prod_key` in `~/.vault_ids/`:

In `~/.ansible.cfg`:
```
[defaults]
vault_identity_list = $prod@~/.vault_ids/prod_key
```

Now lets create the above-referenced file with a password populated:
```
# echo "$(openssl rand -hex 32)" > ~/.vault_ids/prod_key
```
Now lets test creating a vault:
```
# ansible-vault create --encrypt-vault-id prod prod_secrets.yml
```
If we want to create a new vault id named `dev` using the same method, we can do that too:

In `~/.ansible.cfg`:
```
[defaults]
vault_identity_list = $prod@~/.vault_ids/prod_key,$dev@~/.vault_ids/dev_key
```
Time to create a new key too:
```
# echo "$(openssl rand -hex 32)" > ~/.vault_ids/dev_key
```
And now we can use the `dev` id for a different vault:
```
# ansible-vault create --encrypt-vault-id dev dev_secrets.yml
```
## References

[NetworkToCode](https://www.networktocode.com/blog/post/ansible-vault-primer/)
