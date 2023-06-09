# ansible

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&amp;logoColor=white)](https://github.com/rolehippie/ansible)
[![General Workflow](https://github.com/rolehippie/ansible/actions/workflows/general.yml/badge.svg)](https://github.com/rolehippie/ansible/actions/workflows/general.yml)
[![Readme Workflow](https://github.com/rolehippie/ansible/actions/workflows/readme.yml/badge.svg)](https://github.com/rolehippie/ansible/actions/workflows/readme.yml)
[![Galaxy Workflow](https://github.com/rolehippie/ansible/actions/workflows/galaxy.yml/badge.svg)](https://github.com/rolehippie/ansible/actions/workflows/galaxy.yml)
[![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/ansible)](https://github.com/rolehippie/ansible/blob/master/LICENSE)
[![Ansible Role](https://img.shields.io/badge/role-rolehippie.ansible-blue)](https://galaxy.ansible.com/rolehippie/ansible)

Ansible role to install tools around ansible role development.

## Sponsor

Building and improving this Ansible role have been sponsored by my current and previous employers like **[Cloudpunks GmbH](https://cloudpunks.de)** and **[Proact Deutschland GmbH](https://www.proact.eu)**.

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [ansible_extra_molecule](#ansible_extra_molecule)
  - [ansible_extra_packages](#ansible_extra_packages)
  - [ansible_extra_pips](#ansible_extra_pips)
  - [ansible_general_molecule](#ansible_general_molecule)
  - [ansible_general_packages](#ansible_general_packages)
  - [ansible_general_pips](#ansible_general_pips)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.10`


## Default Variables

### ansible_extra_molecule

List of extra molecule

#### Default value

```YAML
ansible_extra_molecule: []
```

#### Example usage

```YAML
ansible_extra_molecule:
  - foo
  - name: bar
    version: 1.0.0
```

### ansible_extra_packages

List of extra packages

#### Default value

```YAML
ansible_extra_packages: []
```

#### Example usage

```YAML
ansible_extra_packages:
  - foo
  - bar
  - baz
```

### ansible_extra_pips

List of extra pips

#### Default value

```YAML
ansible_extra_pips: []
```

#### Example usage

```YAML
ansible_extra_pips:
  - foo
  - name: bar
    version: 1.0.0
```

### ansible_general_molecule

List of general molecule

#### Default value

```YAML
ansible_general_molecule:
  - testinfra
  - molecule
  - molecule-hetznercloud
  - molecule-libvirt
  - molecule-docker
```

#### Example usage

```YAML
ansible_general_molecule:
  - foo
  - name: bar
    version: 1.0.0
```

### ansible_general_packages

List of general packages

#### Default value

```YAML
ansible_general_packages:
  - python3-pip
```

#### Example usage

```YAML
ansible_general_packages:
  - foo
  - bar
  - baz
```

### ansible_general_pips

List of general pips

#### Default value

```YAML
ansible_general_pips:
  - ansible-lint
  - ansible-doctor
  - ansible-later
```

#### Example usage

```YAML
ansible_general_pips:
  - foo
  - name: bar
    version: 1.0.0
```

## Discovered Tags

**_ansible_**


## Dependencies

- None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
