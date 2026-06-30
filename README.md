# Morris Worm Investigation

This is a CyberRangeCZ/KYPO-style training skeleton inspired by the Morris Worm labs from SEED Labs and the uploaded Morris Attack / Morris Forensics slides.

The scenario is intentionally safe. It does **not** deploy a real worm, real shellcode, or a real exploitation chain. Instead, it creates observable artifacts that allow trainees to practice:

- process investigation with `ps`, `pstree`, and `systemctl`
- network investigation with `ss`, `netstat`, `nmap`, and `tcpdump`
- artifact investigation under `/opt/morris`
- timestamp analysis with `stat`

## Topology

- `attacker` on `10.10.10.5`
- `analyst` on `10.30.30.5`
- `victim1` on `10.20.20.11`
- `victim2` on `10.20.20.12`
- `victim3` on `10.20.20.13`
- `router` connects the three networks

## Provisioning

Ansible files are under `provisioning/`, following the common CyberRangeCZ layout:

```text
provisioning/
├── ansible.cfg
├── playbook.yml
├── requirements.yml
├── host_vars/
└── roles/
```

## Notes

You should validate field names in `training.json` against the exact KYPO version you are importing into, because some official libraries use slightly different JSON schemas.
