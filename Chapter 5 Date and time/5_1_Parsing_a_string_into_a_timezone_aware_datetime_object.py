

import dateutil.parser
import datetime

# python 3
dt = datetime.datetime.strptime(
    "2016-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")


# older version of python
dt = dateutil.parser.parse("2016-04-15T08:27:18-0500")

# datetime.datetime(2016, 4, 15, 8, 27, 18, tzinfo=tzoffset(None, -18000))
