# Morris Worm Forensics

A CyberRangeCZ/KYPO-style training library inspired by the Morris Worm investigation lesson.

This version follows the layout used by the public CyberRangeCZ training libraries:

- `topology.yml` and `training.json` are in the repository root.
- `playbook.yml`, `requirements.yml`, and `ansible.cfg` are in `provisioning/`.
- Host-specific provisioning is placed in Ansible roles under `provisioning/roles/`.

The lab is intentionally safe. It does not contain real worm source code, shellcode, or exploit code. The server contains inert artifacts that let learners practice process, network, and timestamp investigation.

## Machines

- `attacker`: contains attacker-side notes and tools.
- `client`: analyst workstation.
- `server`: infected host with the Morris-style artifacts.

## Credentials created by provisioning

- `morris:morris` on attacker
- `analyst:analyst` on client
- `victim:victim` on server

These users are created with the same Ansible style used in CyberRangeCZ examples:

```yaml
password: "{{ 'password' | password_hash('sha512') }}"
```
