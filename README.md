# ansible

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/ansible)
[![General Workflow](https://github.com/rolehippie/ansible/actions/workflows/general.yml/badge.svg)](https://github.com/rolehippie/ansible/actions/workflows/general.yml)
[![Readme Workflow](https://github.com/rolehippie/ansible/actions/workflows/docs.yml/badge.svg)](https://github.com/rolehippie/ansible/actions/workflows/docs.yml)
[![Galaxy Workflow](https://github.com/rolehippie/ansible/actions/workflows/galaxy.yml/badge.svg)](https://github.com/rolehippie/ansible/actions/workflows/galaxy.yml)
[![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/ansible)](https://github.com/rolehippie/ansible/blob/master/LICENSE)
[![Ansible Role](https://img.shields.io/badge/role-rolehippie.ansible-blue)](https://galaxy.ansible.com/rolehippie/ansible)

Ansible role to install tools around ansible role development.

## Sponsor

Building and improving this Ansible role have been sponsored by my current and previous employers like **[Cloudpunks GmbH](https://cloudpunks.de)** and **[Proact Deutschland GmbH](https://www.proact.eu)**.

## Table of contents

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [ansible_doctor_version](#ansible_doctor_version)
  - [ansible_extra_molecule](#ansible_extra_molecule)
  - [ansible_extra_packages](#ansible_extra_packages)
  - [ansible_extra_pips](#ansible_extra_pips)
  - [ansible_general_molecule](#ansible_general_molecule)
  - [ansible_general_packages](#ansible_general_packages)
  - [ansible_general_pips](#ansible_general_pips)
  - [ansible_later_version](#ansible_later_version)
  - [ansible_lint_version](#ansible_lint_version)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.10`

## Default Variables

### ansible_doctor_version

Version of ansible-doctor to install

#### Default value

```YAML
ansible_doctor_version: 2.1.1
```

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
  - molecule-plugins
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
  - name: ansible-doctor
    version: '{{ ansible_doctor_version }}'
  - name: ansible-later
    version: "{{ '2.0.23' if ansible_python_version is version('3.8.100', '<=') else
      ansible_later_version }}"
  - name: ansible-lint
    version: "{{ '6.13.1' if ansible_python_version is version('3.8.100', '<=') else
      ansible_lint_version }}"
```

#### Example usage

```YAML
ansible_general_pips:
  - foo
  - name: bar
    version: 1.0.0
```

### ansible_later_version

Version of ansible-later to install

#### Default value

```YAML
ansible_later_version: 3.3.7
```

### ansible_lint_version

Version of ansible-lint to install

#### Default value

```YAML
ansible_lint_version: 6.17.2
```

## Discovered Tags

**_ansible_**

## Dependencies

- None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
