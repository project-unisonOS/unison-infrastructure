# Key custody, backup, and replacement restore

Status: operational design; software-simulation evidence only

## Provision

1. Install Ubuntu on an encrypted system volume and record the named hardware,
   firmware, secure-boot, TPM, and storage inventory.
2. Select a custody provider. `mounted-file-simulation` is development-only;
   appliance activation requires a reviewed `systemd-credential`, TPM2-sealed,
   or HSM implementation.
3. Generate the root key locally. Never place it in Git, Compose, an environment
   variable, logs, backup-provider storage, or the application database.
4. Mount it at `/run/credentials/unison/root-key`, owned by the service UID with
   mode `0600`. Start services only after the broker validates the file.
5. Keep the independent recovery authority offline and physically separate.

## Back up

1. Create person- or shared-space-scoped provider-blind snapshots only for
   records whose governance permits backup.
2. Verify signed manifest lineage, every retained encrypted object, and the
   independent checkpoint witness.
3. Store the operational journal and checkpoint witness outside the blob
   provider's authority. Alert on missed verification or an expired drill.

## Restore

1. Start from a clean replacement installation with no copied device secrets.
2. Require the local, non-voice recovery ceremony and current checkpoint proof.
3. Run a dry restore and verify scope, lineage, signatures, object integrity,
   and expected record counts before activation.
4. Activate restored state transactionally, revoke the replaced device, rotate
   personal backup authority, and rewrap shared-space keys for current members.
5. Verify private isolation, deletion/tombstone behavior, and a new backup before
   closing the incident.

## Rotate or recover

Use dual control: stage a new root, verify decryption and rewrap capability,
activate it, create and verify a fresh snapshot, then revoke the old authority.
If any check fails, retain the prior root and restore the last verified
checkpoint. Destruction of the last usable root without a tested recovery key
is prohibited.

## Evidence boundary

The committed profile and tests validate configuration, secret-file handling,
provider-blind backup, and replacement-restore software paths. They do not prove
TPM/HSM sealing, encrypted-volume resistance, physical theft protection, or a
human recovery ceremony until the named appliance exists and a witnessed drill
is recorded.
