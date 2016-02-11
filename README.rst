Octopush API Python
=========================

|Build Status|

A Python library for `Octopush API <http://www.octopush.com/en/sms-api>`__.

Octopush offers a solution that was built in-house as a hosted service (SaaS, Software as a Service and an API)
to allow marketing departments of major groups, advertising agencies and IT companies to enjoy an infrastructure
that supports sending SMS messages to more than 200 countries.

Installation
------------

Install via PyPI

.. code:: shell

    pip install octopush

Or add ``octopush`` to your application's `requirements
file <https://pip.pypa.io/en/stable/user_guide/#requirements-files>`__
and then run

.. code:: shell

    pip install -r requirements.txt

Or from source code

.. code:: shell

    git clone https://github.com/bearburger/octopush-api-python.git
    cd octopush-api-python
    python setup.py install

Usage
-----

Config file (``config.py``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    import octopush
    import datetime

    config = {
        'user_login': '*******@*******',
        'api_key': '****************',
        'sms_recipients': ['+33600000000'],
        'sms_text': 'test text ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        'sms_type': octopush.SMS_WORLD,
        'sms_sender': 'onesender'
    }

Balance check
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from octopush import SMS
    from config import config

    sms = SMS(config['user_login'], config['api_key'])

    result = sms.get_credit()

    for credit in result.findall('credit'):
        print(credit.text)

SMS sending
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from octopush import SMS
    from config import config
    import uuid

    sms = SMS(config['user_login'], config['api_key'])
    sms.set_sms_text(config['sms_text'])
    sms.set_sms_recipients(config['sms_recipients'])
    sms.set_sms_type(config['sms_type'])
    sms.set_sms_sender(config['sms_sender'])
    sms.set_sms_request_id(str(uuid.uuid1()))

    result = sms.send()

    print(result)

More examples can be found in `Simple Examples`_ and `Advanced Examples`_.

Requirements
------------

-  API key, register at `octopush.com`_ to get one
-  Python 2.6+, 3.5+
-  `python-requests`_

Documentation
~~~~~~~~~~~~~

This library is completely documented using `PyDoc`_ and will show
autocompletions in all editors that supports it. Alternatively you can
build HTML version of documentation via `pydoc` tool.

API documentation available on `Octopush API documentation portal`_.

.. _Simple Examples: examples/simple_examples/
.. _Advanced Examples: examples/advanced_examples/
.. _octopush.com: http://www.octopush.com/en/registration
.. _python-requests: http://docs.python-requests.org/en/master/
.. _PyDoc: https://docs.python.org/2/library/pydoc.html
.. _Octopush API documentation portal: http://www.octopush.com/en/api-sms-documentation
.. |Build Status| image:: https://travis-ci.org/bearburger/octopush-api-python.png?branch=master
   :target: https://travis-ci.org/bearburger/octopush-api-python
