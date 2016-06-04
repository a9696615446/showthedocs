  $ . $TESTDIR/setup.t.bash

  $ export CONFIG=$TMPDIR/config.py
  $ cat <<EOF > $CONFIG
  > from showdocs import config
  > config.update({
  >     'EXTERNAL_DIR': "$TMPDIR/external",
  >     'LOG': False,
  >     })
  > EOF
  $ getdocs.py list
  nginx
  postgres
  $ getdocs.py build --lang foo
  unknown lang 'foo', known languages: nginx, postgres
  [1]
