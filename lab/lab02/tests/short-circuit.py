test = {
  'name': 'The Truth Will Prevail',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> True and 13
          13
          >>> False or 0
          0
          >>> not 10
          False
          >>> not None
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> True and 1 / 0  # If this errors, just type Error.
          Error
          >>> True or 1 / 0  # If this errors, just type Error.
          True
          >>> -1 and 1 > 0 # If this errors, just type Error.
          True
          >>> -1 or 5
          -1
          >>> (1 + 1) and 1  # If this errors, just type Error. If this is blank, just type Nothing.
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> print(3) or ""
          3
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> def f(x):
          ...     if x == 0:
          ...         return "I am zero!"
          ...     elif x > 0:
          ...         return "Positive!"
          ...     else:
          ...         return ""
          >>> 0 or f(1)
          9a2e04cae090a0414fd465ef7438b6ba
          # locked
          >>> f(0) or f(-1)
          8f5c5b9046dac655b195173d7228bfd1
          # locked
          >>> f(0) and f(-1)
          c8d065903354f375f887443cb1120aca
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
