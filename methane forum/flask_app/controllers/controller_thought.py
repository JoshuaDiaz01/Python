from flask import render_template, session,redirect, request, flash, jsonify
import re
from flask_bcrypt import Bcrypt
from flask_app import app

#this one will change
from flask_app.models import model_thought
from flask_app.models import model_user
bcrypt = Bcrypt(app)

#create newsomething
@app.route('/api/thought/new')
def api_thought():
    data = {
    "methane": [
        {
            "date": "1983.7",
            "average": "1626.0",
            "trend": "1635.6",
            "averageUnc": "2.3",
            "trendUnc": "1.5"
        },
        {
            "date": "1983.8",
            "average": "1628.0",
            "trend": "1636.0",
            "averageUnc": "2.9",
            "trendUnc": "1.4"
        },
        {
            "date": "1983.9",
            "average": "1638.5",
            "trend": "1636.5",
            "averageUnc": "2.3",
            "trendUnc": "1.3"
        },
        {
            "date": "1983.10",
            "average": "1644.8",
            "trend": "1637.1",
            "averageUnc": "1.4",
            "trendUnc": "1.2"
        },
        {
            "date": "1983.11",
            "average": "1642.6",
            "trend": "1637.7",
            "averageUnc": "0.8",
            "trendUnc": "1.2"
        },
        {
            "date": "1983.12",
            "average": "1639.5",
            "trend": "1638.3",
            "averageUnc": "1.0",
            "trendUnc": "1.1"
        },
        {
            "date": "1984.1",
            "average": "1638.7",
            "trend": "1639.1",
            "averageUnc": "1.9",
            "trendUnc": "1.0"
        },
        {
            "date": "1984.2",
            "average": "1638.8",
            "trend": "1639.9",
            "averageUnc": "2.1",
            "trendUnc": "0.9"
        },
        {
            "date": "1984.3",
            "average": "1640.8",
            "trend": "1640.8",
            "averageUnc": "1.5",
            "trendUnc": "0.8"
        },
        {
            "date": "1984.4",
            "average": "1643.7",
            "trend": "1641.8",
            "averageUnc": "1.9",
            "trendUnc": "0.7"
        },
        {
            "date": "1984.5",
            "average": "1642.9",
            "trend": "1642.9",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "1984.6",
            "average": "1639.6",
            "trend": "1644.0",
            "averageUnc": "0.8",
            "trendUnc": "0.7"
        },
        {
            "date": "1984.7",
            "average": "1637.8",
            "trend": "1645.2",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1984.8",
            "average": "1641.3",
            "trend": "1646.4",
            "averageUnc": "1.4",
            "trendUnc": "0.6"
        },
        {
            "date": "1984.9",
            "average": "1650.4",
            "trend": "1647.5",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1984.10",
            "average": "1654.5",
            "trend": "1648.7",
            "averageUnc": "1.4",
            "trendUnc": "0.6"
        },
        {
            "date": "1984.11",
            "average": "1653.7",
            "trend": "1649.8",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1984.12",
            "average": "1656.1",
            "trend": "1651.0",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "1985.1",
            "average": "1655.6",
            "trend": "1652.1",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "1985.2",
            "average": "1652.2",
            "trend": "1653.1",
            "averageUnc": "1.5",
            "trendUnc": "0.6"
        },
        {
            "date": "1985.3",
            "average": "1654.6",
            "trend": "1654.1",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1985.4",
            "average": "1658.2",
            "trend": "1655.2",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1985.5",
            "average": "1655.9",
            "trend": "1656.2",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "1985.6",
            "average": "1650.1",
            "trend": "1657.2",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "1985.7",
            "average": "1646.8",
            "trend": "1658.2",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "1985.8",
            "average": "1652.2",
            "trend": "1659.2",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "1985.9",
            "average": "1662.5",
            "trend": "1660.2",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "1985.10",
            "average": "1667.5",
            "trend": "1661.2",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1985.11",
            "average": "1666.8",
            "trend": "1662.2",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1985.12",
            "average": "1666.1",
            "trend": "1663.3",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1986.1",
            "average": "1666.2",
            "trend": "1664.3",
            "averageUnc": "1.2",
            "trendUnc": "0.7"
        },
        {
            "date": "1986.2",
            "average": "1666.9",
            "trend": "1665.3",
            "averageUnc": "2.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1986.3",
            "average": "1669.3",
            "trend": "1666.4",
            "averageUnc": "1.5",
            "trendUnc": "0.7"
        },
        {
            "date": "1986.4",
            "average": "1670.8",
            "trend": "1667.4",
            "averageUnc": "1.5",
            "trendUnc": "0.8"
        },
        {
            "date": "1986.5",
            "average": "1668.4",
            "trend": "1668.5",
            "averageUnc": "0.9",
            "trendUnc": "0.8"
        },
        {
            "date": "1986.6",
            "average": "1664.8",
            "trend": "1669.6",
            "averageUnc": "1.3",
            "trendUnc": "0.8"
        },
        {
            "date": "1986.7",
            "average": "1662.3",
            "trend": "1670.7",
            "averageUnc": "1.2",
            "trendUnc": "0.8"
        },
        {
            "date": "1986.8",
            "average": "1664.3",
            "trend": "1671.8",
            "averageUnc": "1.6",
            "trendUnc": "0.8"
        },
        {
            "date": "1986.9",
            "average": "1672.6",
            "trend": "1672.9",
            "averageUnc": "1.5",
            "trendUnc": "0.8"
        },
        {
            "date": "1986.10",
            "average": "1678.7",
            "trend": "1674.0",
            "averageUnc": "1.5",
            "trendUnc": "0.8"
        },
        {
            "date": "1986.11",
            "average": "1679.0",
            "trend": "1675.1",
            "averageUnc": "1.7",
            "trendUnc": "0.8"
        },
        {
            "date": "1986.12",
            "average": "1679.1",
            "trend": "1676.2",
            "averageUnc": "1.2",
            "trendUnc": "0.8"
        },
        {
            "date": "1987.1",
            "average": "1679.3",
            "trend": "1677.3",
            "averageUnc": "1.2",
            "trendUnc": "0.8"
        },
        {
            "date": "1987.2",
            "average": "1679.0",
            "trend": "1678.3",
            "averageUnc": "1.1",
            "trendUnc": "0.8"
        },
        {
            "date": "1987.3",
            "average": "1680.1",
            "trend": "1679.3",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "1987.4",
            "average": "1681.4",
            "trend": "1680.4",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1987.5",
            "average": "1681.9",
            "trend": "1681.4",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1987.6",
            "average": "1680.0",
            "trend": "1682.4",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1987.7",
            "average": "1676.0",
            "trend": "1683.3",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1987.8",
            "average": "1677.1",
            "trend": "1684.3",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1987.9",
            "average": "1685.6",
            "trend": "1685.2",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "1987.10",
            "average": "1691.6",
            "trend": "1686.0",
            "averageUnc": "1.1",
            "trendUnc": "0.4"
        },
        {
            "date": "1987.11",
            "average": "1691.1",
            "trend": "1686.9",
            "averageUnc": "0.8",
            "trendUnc": "0.4"
        },
        {
            "date": "1987.12",
            "average": "1690.5",
            "trend": "1687.7",
            "averageUnc": "0.9",
            "trendUnc": "0.4"
        },
        {
            "date": "1988.1",
            "average": "1691.9",
            "trend": "1688.5",
            "averageUnc": "0.7",
            "trendUnc": "0.4"
        },
        {
            "date": "1988.2",
            "average": "1692.5",
            "trend": "1689.3",
            "averageUnc": "0.8",
            "trendUnc": "0.4"
        },
        {
            "date": "1988.3",
            "average": "1691.3",
            "trend": "1690.1",
            "averageUnc": "1.0",
            "trendUnc": "0.4"
        },
        {
            "date": "1988.4",
            "average": "1690.0",
            "trend": "1690.9",
            "averageUnc": "0.9",
            "trendUnc": "0.4"
        },
        {
            "date": "1988.5",
            "average": "1689.0",
            "trend": "1691.8",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1988.6",
            "average": "1687.1",
            "trend": "1692.7",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "1988.7",
            "average": "1685.9",
            "trend": "1693.5",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1988.8",
            "average": "1689.3",
            "trend": "1694.5",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1988.9",
            "average": "1696.3",
            "trend": "1695.4",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1988.10",
            "average": "1701.3",
            "trend": "1696.4",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1988.11",
            "average": "1702.9",
            "trend": "1697.4",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "1988.12",
            "average": "1702.0",
            "trend": "1698.4",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1989.1",
            "average": "1700.6",
            "trend": "1699.4",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1989.2",
            "average": "1701.1",
            "trend": "1700.4",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1989.3",
            "average": "1702.5",
            "trend": "1701.4",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1989.4",
            "average": "1703.7",
            "trend": "1702.4",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1989.5",
            "average": "1703.4",
            "trend": "1703.4",
            "averageUnc": "0.6",
            "trendUnc": "0.6"
        },
        {
            "date": "1989.6",
            "average": "1700.3",
            "trend": "1704.4",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1989.7",
            "average": "1698.2",
            "trend": "1705.3",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1989.8",
            "average": "1702.0",
            "trend": "1706.2",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1989.9",
            "average": "1707.2",
            "trend": "1707.1",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1989.10",
            "average": "1710.5",
            "trend": "1708.0",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "1989.11",
            "average": "1713.1",
            "trend": "1708.8",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1989.12",
            "average": "1713.2",
            "trend": "1709.6",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1990.1",
            "average": "1712.0",
            "trend": "1710.4",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1990.2",
            "average": "1713.3",
            "trend": "1711.1",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1990.3",
            "average": "1714.4",
            "trend": "1711.7",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "1990.4",
            "average": "1712.6",
            "trend": "1712.4",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "1990.5",
            "average": "1710.7",
            "trend": "1713.1",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "1990.6",
            "average": "1708.3",
            "trend": "1713.8",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "1990.7",
            "average": "1706.4",
            "trend": "1714.4",
            "averageUnc": "0.8",
            "trendUnc": "0.7"
        },
        {
            "date": "1990.8",
            "average": "1710.1",
            "trend": "1715.1",
            "averageUnc": "1.2",
            "trendUnc": "0.7"
        },
        {
            "date": "1990.9",
            "average": "1717.6",
            "trend": "1715.8",
            "averageUnc": "1.2",
            "trendUnc": "0.7"
        },
        {
            "date": "1990.10",
            "average": "1722.0",
            "trend": "1716.6",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "1990.11",
            "average": "1723.5",
            "trend": "1717.4",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1990.12",
            "average": "1723.4",
            "trend": "1718.2",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1991.1",
            "average": "1721.6",
            "trend": "1719.2",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1991.2",
            "average": "1721.2",
            "trend": "1720.2",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "1991.3",
            "average": "1722.1",
            "trend": "1721.2",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1991.4",
            "average": "1722.5",
            "trend": "1722.4",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1991.5",
            "average": "1722.2",
            "trend": "1723.6",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1991.6",
            "average": "1719.0",
            "trend": "1724.9",
            "averageUnc": "1.2",
            "trendUnc": "0.7"
        },
        {
            "date": "1991.7",
            "average": "1716.1",
            "trend": "1726.2",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1991.8",
            "average": "1719.2",
            "trend": "1727.5",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "1991.9",
            "average": "1726.2",
            "trend": "1728.8",
            "averageUnc": "1.3",
            "trendUnc": "0.7"
        },
        {
            "date": "1991.10",
            "average": "1732.7",
            "trend": "1730.1",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1991.11",
            "average": "1737.5",
            "trend": "1731.2",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "1991.12",
            "average": "1739.7",
            "trend": "1732.3",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "1992.1",
            "average": "1738.9",
            "trend": "1733.2",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "1992.2",
            "average": "1737.3",
            "trend": "1734.0",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "1992.3",
            "average": "1737.0",
            "trend": "1734.6",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1992.4",
            "average": "1736.6",
            "trend": "1735.1",
            "averageUnc": "0.6",
            "trendUnc": "0.6"
        },
        {
            "date": "1992.5",
            "average": "1734.9",
            "trend": "1735.4",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "1992.6",
            "average": "1731.6",
            "trend": "1735.6",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1992.7",
            "average": "1728.9",
            "trend": "1735.7",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1992.8",
            "average": "1730.4",
            "trend": "1735.7",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1992.9",
            "average": "1734.7",
            "trend": "1735.6",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1992.10",
            "average": "1737.8",
            "trend": "1735.4",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1992.11",
            "average": "1739.3",
            "trend": "1735.3",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "1992.12",
            "average": "1738.6",
            "trend": "1735.2",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1993.1",
            "average": "1735.8",
            "trend": "1735.1",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1993.2",
            "average": "1734.4",
            "trend": "1735.1",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "1993.3",
            "average": "1735.5",
            "trend": "1735.2",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1993.4",
            "average": "1736.7",
            "trend": "1735.3",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1993.5",
            "average": "1735.0",
            "trend": "1735.5",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1993.6",
            "average": "1730.9",
            "trend": "1735.8",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1993.7",
            "average": "1728.0",
            "trend": "1736.2",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1993.8",
            "average": "1731.2",
            "trend": "1736.6",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1993.9",
            "average": "1738.5",
            "trend": "1737.1",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1993.10",
            "average": "1743.3",
            "trend": "1737.6",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1993.11",
            "average": "1745.2",
            "trend": "1738.1",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "1993.12",
            "average": "1744.3",
            "trend": "1738.7",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.1",
            "average": "1741.4",
            "trend": "1739.3",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.2",
            "average": "1740.9",
            "trend": "1739.8",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.3",
            "average": "1741.9",
            "trend": "1740.4",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.4",
            "average": "1741.9",
            "trend": "1741.0",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.5",
            "average": "1740.6",
            "trend": "1741.6",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.6",
            "average": "1736.9",
            "trend": "1742.2",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.7",
            "average": "1732.4",
            "trend": "1742.9",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.8",
            "average": "1734.1",
            "trend": "1743.5",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.9",
            "average": "1743.0",
            "trend": "1744.1",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.10",
            "average": "1749.8",
            "trend": "1744.7",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.11",
            "average": "1751.2",
            "trend": "1745.3",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.12",
            "average": "1751.6",
            "trend": "1745.9",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1995.1",
            "average": "1751.0",
            "trend": "1746.5",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1995.2",
            "average": "1749.4",
            "trend": "1747.0",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1995.3",
            "average": "1748.9",
            "trend": "1747.5",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "1995.4",
            "average": "1749.4",
            "trend": "1747.9",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "1995.5",
            "average": "1747.7",
            "trend": "1748.3",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "1995.6",
            "average": "1742.8",
            "trend": "1748.7",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1995.7",
            "average": "1740.1",
            "trend": "1749.0",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1995.8",
            "average": "1743.5",
            "trend": "1749.2",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "1995.9",
            "average": "1749.7",
            "trend": "1749.5",
            "averageUnc": "1.3",
            "trendUnc": "0.5"
        },
        {
            "date": "1995.10",
            "average": "1754.2",
            "trend": "1749.7",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1995.11",
            "average": "1755.3",
            "trend": "1749.9",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1995.12",
            "average": "1753.7",
            "trend": "1750.1",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1996.1",
            "average": "1752.3",
            "trend": "1750.2",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1996.2",
            "average": "1752.9",
            "trend": "1750.4",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1996.3",
            "average": "1752.4",
            "trend": "1750.6",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1996.4",
            "average": "1749.9",
            "trend": "1750.8",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1996.5",
            "average": "1748.6",
            "trend": "1751.0",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "1996.6",
            "average": "1746.2",
            "trend": "1751.2",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1996.7",
            "average": "1742.2",
            "trend": "1751.4",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "1996.8",
            "average": "1744.7",
            "trend": "1751.7",
            "averageUnc": "1.3",
            "trendUnc": "0.7"
        },
        {
            "date": "1996.9",
            "average": "1753.0",
            "trend": "1751.9",
            "averageUnc": "1.3",
            "trendUnc": "0.7"
        },
        {
            "date": "1996.10",
            "average": "1759.0",
            "trend": "1752.1",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1996.11",
            "average": "1759.9",
            "trend": "1752.3",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1996.12",
            "average": "1756.8",
            "trend": "1752.5",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "1997.1",
            "average": "1753.4",
            "trend": "1752.8",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1997.2",
            "average": "1753.8",
            "trend": "1753.0",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1997.3",
            "average": "1755.6",
            "trend": "1753.2",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1997.4",
            "average": "1755.5",
            "trend": "1753.5",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1997.5",
            "average": "1753.9",
            "trend": "1753.9",
            "averageUnc": "0.7",
            "trendUnc": "0.4"
        },
        {
            "date": "1997.6",
            "average": "1750.2",
            "trend": "1754.2",
            "averageUnc": "0.9",
            "trendUnc": "0.4"
        },
        {
            "date": "1997.7",
            "average": "1746.2",
            "trend": "1754.7",
            "averageUnc": "1.0",
            "trendUnc": "0.4"
        },
        {
            "date": "1997.8",
            "average": "1747.9",
            "trend": "1755.3",
            "averageUnc": "0.9",
            "trendUnc": "0.4"
        },
        {
            "date": "1997.9",
            "average": "1755.1",
            "trend": "1755.9",
            "averageUnc": "0.9",
            "trendUnc": "0.4"
        },
        {
            "date": "1997.10",
            "average": "1760.2",
            "trend": "1756.6",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1997.11",
            "average": "1761.7",
            "trend": "1757.5",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1997.12",
            "average": "1761.9",
            "trend": "1758.4",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1998.1",
            "average": "1761.5",
            "trend": "1759.4",
            "averageUnc": "0.7",
            "trendUnc": "0.5"
        },
        {
            "date": "1998.2",
            "average": "1761.5",
            "trend": "1760.5",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "1998.3",
            "average": "1763.0",
            "trend": "1761.6",
            "averageUnc": "1.6",
            "trendUnc": "0.6"
        },
        {
            "date": "1998.4",
            "average": "1764.7",
            "trend": "1762.8",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "1998.5",
            "average": "1764.2",
            "trend": "1764.0",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1998.6",
            "average": "1760.3",
            "trend": "1765.1",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "1998.7",
            "average": "1756.1",
            "trend": "1766.3",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1998.8",
            "average": "1760.1",
            "trend": "1767.4",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1998.9",
            "average": "1770.5",
            "trend": "1768.4",
            "averageUnc": "1.3",
            "trendUnc": "0.7"
        },
        {
            "date": "1998.10",
            "average": "1776.2",
            "trend": "1769.3",
            "averageUnc": "1.3",
            "trendUnc": "0.7"
        },
        {
            "date": "1998.11",
            "average": "1775.6",
            "trend": "1770.1",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "1998.12",
            "average": "1774.2",
            "trend": "1770.7",
            "averageUnc": "0.8",
            "trendUnc": "0.7"
        },
        {
            "date": "1999.1",
            "average": "1774.0",
            "trend": "1771.3",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1999.2",
            "average": "1774.2",
            "trend": "1771.8",
            "averageUnc": "1.5",
            "trendUnc": "0.7"
        },
        {
            "date": "1999.3",
            "average": "1774.7",
            "trend": "1772.2",
            "averageUnc": "1.2",
            "trendUnc": "0.7"
        },
        {
            "date": "1999.4",
            "average": "1774.9",
            "trend": "1772.5",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "1999.5",
            "average": "1772.7",
            "trend": "1772.8",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1999.6",
            "average": "1767.4",
            "trend": "1773.0",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "1999.7",
            "average": "1763.0",
            "trend": "1773.1",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "1999.8",
            "average": "1764.7",
            "trend": "1773.2",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1999.9",
            "average": "1771.1",
            "trend": "1773.3",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "1999.10",
            "average": "1776.6",
            "trend": "1773.4",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "1999.11",
            "average": "1778.6",
            "trend": "1773.4",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "1999.12",
            "average": "1777.3",
            "trend": "1773.4",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2000.1",
            "average": "1775.7",
            "trend": "1773.5",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2000.2",
            "average": "1775.8",
            "trend": "1773.5",
            "averageUnc": "1.4",
            "trendUnc": "0.7"
        },
        {
            "date": "2000.3",
            "average": "1776.9",
            "trend": "1773.4",
            "averageUnc": "1.5",
            "trendUnc": "0.7"
        },
        {
            "date": "2000.4",
            "average": "1777.4",
            "trend": "1773.4",
            "averageUnc": "1.4",
            "trendUnc": "0.7"
        },
        {
            "date": "2000.5",
            "average": "1774.6",
            "trend": "1773.3",
            "averageUnc": "1.2",
            "trendUnc": "0.8"
        },
        {
            "date": "2000.6",
            "average": "1768.2",
            "trend": "1773.2",
            "averageUnc": "1.1",
            "trendUnc": "0.8"
        },
        {
            "date": "2000.7",
            "average": "1763.6",
            "trend": "1773.1",
            "averageUnc": "0.8",
            "trendUnc": "0.8"
        },
        {
            "date": "2000.8",
            "average": "1765.7",
            "trend": "1772.9",
            "averageUnc": "1.0",
            "trendUnc": "0.8"
        },
        {
            "date": "2000.9",
            "average": "1772.2",
            "trend": "1772.7",
            "averageUnc": "1.1",
            "trendUnc": "0.8"
        },
        {
            "date": "2000.10",
            "average": "1777.1",
            "trend": "1772.5",
            "averageUnc": "0.8",
            "trendUnc": "0.7"
        },
        {
            "date": "2000.11",
            "average": "1777.7",
            "trend": "1772.3",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2000.12",
            "average": "1775.3",
            "trend": "1772.1",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2001.1",
            "average": "1772.9",
            "trend": "1771.9",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "2001.2",
            "average": "1772.5",
            "trend": "1771.7",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2001.3",
            "average": "1773.7",
            "trend": "1771.5",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2001.4",
            "average": "1773.9",
            "trend": "1771.3",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "2001.5",
            "average": "1770.8",
            "trend": "1771.2",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2001.6",
            "average": "1765.9",
            "trend": "1771.1",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2001.7",
            "average": "1762.8",
            "trend": "1771.1",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2001.8",
            "average": "1764.3",
            "trend": "1771.0",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2001.9",
            "average": "1770.5",
            "trend": "1771.0",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "2001.10",
            "average": "1775.5",
            "trend": "1771.1",
            "averageUnc": "0.6",
            "trendUnc": "0.5"
        },
        {
            "date": "2001.11",
            "average": "1776.6",
            "trend": "1771.1",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "2001.12",
            "average": "1775.9",
            "trend": "1771.2",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2002.1",
            "average": "1774.1",
            "trend": "1771.3",
            "averageUnc": "1.2",
            "trendUnc": "0.4"
        },
        {
            "date": "2002.2",
            "average": "1772.8",
            "trend": "1771.4",
            "averageUnc": "1.0",
            "trendUnc": "0.4"
        },
        {
            "date": "2002.3",
            "average": "1773.4",
            "trend": "1771.6",
            "averageUnc": "0.6",
            "trendUnc": "0.4"
        },
        {
            "date": "2002.4",
            "average": "1772.7",
            "trend": "1771.7",
            "averageUnc": "0.6",
            "trendUnc": "0.4"
        },
        {
            "date": "2002.5",
            "average": "1770.3",
            "trend": "1771.9",
            "averageUnc": "0.7",
            "trendUnc": "0.5"
        },
        {
            "date": "2002.6",
            "average": "1766.9",
            "trend": "1772.1",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "2002.7",
            "average": "1764.3",
            "trend": "1772.4",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2002.8",
            "average": "1767.0",
            "trend": "1772.7",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2002.9",
            "average": "1773.8",
            "trend": "1773.0",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2002.10",
            "average": "1778.2",
            "trend": "1773.4",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2002.11",
            "average": "1779.6",
            "trend": "1773.8",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2002.12",
            "average": "1779.7",
            "trend": "1774.2",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2003.1",
            "average": "1777.5",
            "trend": "1774.8",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2003.2",
            "average": "1774.8",
            "trend": "1775.3",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2003.3",
            "average": "1774.8",
            "trend": "1775.8",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2003.4",
            "average": "1775.7",
            "trend": "1776.4",
            "averageUnc": "1.3",
            "trendUnc": "0.5"
        },
        {
            "date": "2003.5",
            "average": "1774.4",
            "trend": "1777.0",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2003.6",
            "average": "1771.7",
            "trend": "1777.5",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "2003.7",
            "average": "1770.7",
            "trend": "1778.0",
            "averageUnc": "1.8",
            "trendUnc": "0.5"
        },
        {
            "date": "2003.8",
            "average": "1774.2",
            "trend": "1778.5",
            "averageUnc": "1.6",
            "trendUnc": "0.5"
        },
        {
            "date": "2003.9",
            "average": "1780.5",
            "trend": "1778.8",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2003.10",
            "average": "1784.7",
            "trend": "1779.1",
            "averageUnc": "0.7",
            "trendUnc": "0.5"
        },
        {
            "date": "2003.11",
            "average": "1785.3",
            "trend": "1779.3",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2003.12",
            "average": "1783.6",
            "trend": "1779.3",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2004.1",
            "average": "1780.9",
            "trend": "1779.2",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2004.2",
            "average": "1779.9",
            "trend": "1779.1",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2004.3",
            "average": "1781.0",
            "trend": "1778.8",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2004.4",
            "average": "1780.7",
            "trend": "1778.4",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2004.5",
            "average": "1777.6",
            "trend": "1777.9",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2004.6",
            "average": "1772.3",
            "trend": "1777.4",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2004.7",
            "average": "1768.0",
            "trend": "1776.9",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2004.8",
            "average": "1769.7",
            "trend": "1776.3",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2004.9",
            "average": "1775.5",
            "trend": "1775.8",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2004.10",
            "average": "1779.7",
            "trend": "1775.3",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2004.11",
            "average": "1780.5",
            "trend": "1774.9",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2004.12",
            "average": "1778.3",
            "trend": "1774.6",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.1",
            "average": "1776.0",
            "trend": "1774.3",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.2",
            "average": "1775.6",
            "trend": "1774.1",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.3",
            "average": "1775.5",
            "trend": "1774.1",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.4",
            "average": "1774.6",
            "trend": "1774.0",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.5",
            "average": "1772.3",
            "trend": "1774.1",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.6",
            "average": "1768.7",
            "trend": "1774.2",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.7",
            "average": "1766.3",
            "trend": "1774.3",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.8",
            "average": "1768.0",
            "trend": "1774.4",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.9",
            "average": "1773.2",
            "trend": "1774.5",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.10",
            "average": "1778.6",
            "trend": "1774.6",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.11",
            "average": "1781.1",
            "trend": "1774.7",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.12",
            "average": "1780.1",
            "trend": "1774.8",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2006.1",
            "average": "1779.4",
            "trend": "1774.8",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2006.2",
            "average": "1779.4",
            "trend": "1774.8",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2006.3",
            "average": "1777.4",
            "trend": "1774.7",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "2006.4",
            "average": "1776.1",
            "trend": "1774.7",
            "averageUnc": "0.7",
            "trendUnc": "0.5"
        },
        {
            "date": "2006.5",
            "average": "1775.0",
            "trend": "1774.7",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2006.6",
            "average": "1769.3",
            "trend": "1774.7",
            "averageUnc": "1.3",
            "trendUnc": "0.5"
        },
        {
            "date": "2006.7",
            "average": "1764.2",
            "trend": "1774.8",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "2006.8",
            "average": "1767.2",
            "trend": "1774.9",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "2006.9",
            "average": "1774.6",
            "trend": "1775.2",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2006.10",
            "average": "1778.2",
            "trend": "1775.5",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2006.11",
            "average": "1779.0",
            "trend": "1775.9",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "2006.12",
            "average": "1779.9",
            "trend": "1776.4",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.1",
            "average": "1779.2",
            "trend": "1777.0",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.2",
            "average": "1778.7",
            "trend": "1777.6",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.3",
            "average": "1780.3",
            "trend": "1778.3",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.4",
            "average": "1781.1",
            "trend": "1779.0",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.5",
            "average": "1779.4",
            "trend": "1779.8",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.6",
            "average": "1775.6",
            "trend": "1780.5",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.7",
            "average": "1772.6",
            "trend": "1781.2",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.8",
            "average": "1777.2",
            "trend": "1781.9",
            "averageUnc": "1.5",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.9",
            "average": "1785.9",
            "trend": "1782.6",
            "averageUnc": "1.5",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.10",
            "average": "1789.9",
            "trend": "1783.2",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.11",
            "average": "1789.5",
            "trend": "1783.7",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2007.12",
            "average": "1788.2",
            "trend": "1784.3",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.1",
            "average": "1786.8",
            "trend": "1784.8",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.2",
            "average": "1785.8",
            "trend": "1785.3",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.3",
            "average": "1786.1",
            "trend": "1785.8",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.4",
            "average": "1786.8",
            "trend": "1786.3",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.5",
            "average": "1785.1",
            "trend": "1786.8",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.6",
            "average": "1780.4",
            "trend": "1787.3",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.7",
            "average": "1777.6",
            "trend": "1787.9",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.8",
            "average": "1781.0",
            "trend": "1788.5",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.9",
            "average": "1787.7",
            "trend": "1789.0",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.10",
            "average": "1793.7",
            "trend": "1789.6",
            "averageUnc": "0.7",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.11",
            "average": "1797.4",
            "trend": "1790.2",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.12",
            "average": "1796.7",
            "trend": "1790.8",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2009.1",
            "average": "1795.1",
            "trend": "1791.4",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2009.2",
            "average": "1795.6",
            "trend": "1791.9",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "2009.3",
            "average": "1796.1",
            "trend": "1792.3",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2009.4",
            "average": "1795.6",
            "trend": "1792.8",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2009.5",
            "average": "1792.3",
            "trend": "1793.2",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "2009.6",
            "average": "1786.9",
            "trend": "1793.6",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2009.7",
            "average": "1784.9",
            "trend": "1794.0",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "2009.8",
            "average": "1788.8",
            "trend": "1794.3",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2009.9",
            "average": "1794.8",
            "trend": "1794.6",
            "averageUnc": "1.2",
            "trendUnc": "0.7"
        },
        {
            "date": "2009.10",
            "average": "1798.0",
            "trend": "1794.9",
            "averageUnc": "1.4",
            "trendUnc": "0.7"
        },
        {
            "date": "2009.11",
            "average": "1797.9",
            "trend": "1795.2",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2009.12",
            "average": "1796.7",
            "trend": "1795.6",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.1",
            "average": "1797.1",
            "trend": "1795.9",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.2",
            "average": "1798.7",
            "trend": "1796.3",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.3",
            "average": "1799.4",
            "trend": "1796.7",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.4",
            "average": "1799.6",
            "trend": "1797.1",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.5",
            "average": "1797.7",
            "trend": "1797.5",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.6",
            "average": "1792.6",
            "trend": "1797.9",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.7",
            "average": "1789.4",
            "trend": "1798.4",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.8",
            "average": "1794.0",
            "trend": "1798.9",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.9",
            "average": "1801.8",
            "trend": "1799.3",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.10",
            "average": "1806.5",
            "trend": "1799.8",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.11",
            "average": "1807.0",
            "trend": "1800.3",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2010.12",
            "average": "1803.6",
            "trend": "1800.7",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.1",
            "average": "1800.5",
            "trend": "1801.2",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.2",
            "average": "1800.2",
            "trend": "1801.6",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.3",
            "average": "1801.0",
            "trend": "1802.0",
            "averageUnc": "0.7",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.4",
            "average": "1802.9",
            "trend": "1802.4",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.5",
            "average": "1803.3",
            "trend": "1802.8",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.6",
            "average": "1799.2",
            "trend": "1803.2",
            "averageUnc": "0.7",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.7",
            "average": "1796.1",
            "trend": "1803.6",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.8",
            "average": "1798.9",
            "trend": "1804.0",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.9",
            "average": "1804.0",
            "trend": "1804.4",
            "averageUnc": "1.6",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.10",
            "average": "1809.5",
            "trend": "1804.8",
            "averageUnc": "1.6",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.11",
            "average": "1812.3",
            "trend": "1805.2",
            "averageUnc": "1.3",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.12",
            "average": "1810.0",
            "trend": "1805.6",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2012.1",
            "average": "1807.3",
            "trend": "1806.0",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2012.2",
            "average": "1808.3",
            "trend": "1806.4",
            "averageUnc": "1.4",
            "trendUnc": "0.7"
        },
        {
            "date": "2012.3",
            "average": "1810.0",
            "trend": "1806.9",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2012.4",
            "average": "1808.4",
            "trend": "1807.3",
            "averageUnc": "0.6",
            "trendUnc": "0.7"
        },
        {
            "date": "2012.5",
            "average": "1804.7",
            "trend": "1807.8",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2012.6",
            "average": "1800.9",
            "trend": "1808.2",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2012.7",
            "average": "1799.2",
            "trend": "1808.6",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2012.8",
            "average": "1803.2",
            "trend": "1809.1",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2012.9",
            "average": "1810.1",
            "trend": "1809.5",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2012.10",
            "average": "1814.7",
            "trend": "1809.9",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2012.11",
            "average": "1815.9",
            "trend": "1810.3",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2012.12",
            "average": "1814.6",
            "trend": "1810.6",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.1",
            "average": "1814.1",
            "trend": "1811.0",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.2",
            "average": "1814.2",
            "trend": "1811.3",
            "averageUnc": "1.6",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.3",
            "average": "1813.3",
            "trend": "1811.6",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.4",
            "average": "1812.8",
            "trend": "1812.0",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.5",
            "average": "1811.9",
            "trend": "1812.3",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.6",
            "average": "1808.5",
            "trend": "1812.7",
            "averageUnc": "1.4",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.7",
            "average": "1805.7",
            "trend": "1813.1",
            "averageUnc": "1.5",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.8",
            "average": "1808.4",
            "trend": "1813.6",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.9",
            "average": "1814.3",
            "trend": "1814.1",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.10",
            "average": "1818.6",
            "trend": "1814.7",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.11",
            "average": "1820.4",
            "trend": "1815.4",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.12",
            "average": "1819.4",
            "trend": "1816.1",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2014.1",
            "average": "1816.9",
            "trend": "1817.0",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2014.2",
            "average": "1816.4",
            "trend": "1817.9",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2014.3",
            "average": "1818.1",
            "trend": "1818.8",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "2014.4",
            "average": "1820.9",
            "trend": "1819.9",
            "averageUnc": "0.6",
            "trendUnc": "0.5"
        },
        {
            "date": "2014.5",
            "average": "1821.9",
            "trend": "1820.9",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "2014.6",
            "average": "1818.4",
            "trend": "1822.1",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "2014.7",
            "average": "1815.6",
            "trend": "1823.2",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2014.8",
            "average": "1819.8",
            "trend": "1824.4",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2014.9",
            "average": "1827.0",
            "trend": "1825.5",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2014.10",
            "average": "1831.3",
            "trend": "1826.6",
            "averageUnc": "0.6",
            "trendUnc": "0.5"
        },
        {
            "date": "2014.11",
            "average": "1833.1",
            "trend": "1827.7",
            "averageUnc": "0.6",
            "trendUnc": "0.5"
        },
        {
            "date": "2014.12",
            "average": "1833.5",
            "trend": "1828.8",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "2015.1",
            "average": "1832.9",
            "trend": "1829.8",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2015.2",
            "average": "1832.7",
            "trend": "1830.7",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "2015.3",
            "average": "1833.1",
            "trend": "1831.6",
            "averageUnc": "0.7",
            "trendUnc": "0.5"
        },
        {
            "date": "2015.4",
            "average": "1833.2",
            "trend": "1832.5",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2015.5",
            "average": "1831.8",
            "trend": "1833.4",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2015.6",
            "average": "1827.4",
            "trend": "1834.2",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2015.7",
            "average": "1824.8",
            "trend": "1835.0",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2015.8",
            "average": "1829.2",
            "trend": "1835.8",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2015.9",
            "average": "1836.2",
            "trend": "1836.6",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2015.10",
            "average": "1841.5",
            "trend": "1837.4",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2015.11",
            "average": "1844.7",
            "trend": "1838.2",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2015.12",
            "average": "1844.9",
            "trend": "1838.9",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2016.1",
            "average": "1842.4",
            "trend": "1839.7",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2016.2",
            "average": "1841.6",
            "trend": "1840.4",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2016.3",
            "average": "1843.0",
            "trend": "1841.0",
            "averageUnc": "0.8",
            "trendUnc": "0.7"
        },
        {
            "date": "2016.4",
            "average": "1843.7",
            "trend": "1841.7",
            "averageUnc": "0.7",
            "trendUnc": "0.7"
        },
        {
            "date": "2016.5",
            "average": "1842.1",
            "trend": "1842.3",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2016.6",
            "average": "1837.9",
            "trend": "1843.0",
            "averageUnc": "1.2",
            "trendUnc": "0.7"
        },
        {
            "date": "2016.7",
            "average": "1834.2",
            "trend": "1843.5",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2016.8",
            "average": "1836.7",
            "trend": "1844.1",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2016.9",
            "average": "1844.2",
            "trend": "1844.6",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2016.10",
            "average": "1849.9",
            "trend": "1845.1",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2016.11",
            "average": "1851.4",
            "trend": "1845.6",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2016.12",
            "average": "1851.1",
            "trend": "1846.1",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2017.1",
            "average": "1849.8",
            "trend": "1846.6",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2017.2",
            "average": "1848.5",
            "trend": "1847.1",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2017.3",
            "average": "1848.3",
            "trend": "1847.6",
            "averageUnc": "1.4",
            "trendUnc": "0.6"
        },
        {
            "date": "2017.4",
            "average": "1848.6",
            "trend": "1848.1",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2017.5",
            "average": "1847.2",
            "trend": "1848.6",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2017.6",
            "average": "1843.0",
            "trend": "1849.2",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2017.7",
            "average": "1840.4",
            "trend": "1849.7",
            "averageUnc": "1.3",
            "trendUnc": "0.7"
        },
        {
            "date": "2017.8",
            "average": "1844.6",
            "trend": "1850.3",
            "averageUnc": "1.2",
            "trendUnc": "0.7"
        },
        {
            "date": "2017.9",
            "average": "1852.8",
            "trend": "1850.9",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "2017.10",
            "average": "1858.1",
            "trend": "1851.6",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2017.11",
            "average": "1858.7",
            "trend": "1852.2",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "2017.12",
            "average": "1856.7",
            "trend": "1852.9",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "2018.1",
            "average": "1854.5",
            "trend": "1853.6",
            "averageUnc": "1.0",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.2",
            "average": "1855.0",
            "trend": "1854.3",
            "averageUnc": "0.9",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.3",
            "average": "1856.9",
            "trend": "1855.0",
            "averageUnc": "0.9",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.4",
            "average": "1856.7",
            "trend": "1855.7",
            "averageUnc": "1.1",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.5",
            "average": "1854.8",
            "trend": "1856.4",
            "averageUnc": "1.6",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.6",
            "average": "1852.0",
            "trend": "1857.2",
            "averageUnc": "1.5",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.7",
            "average": "1849.0",
            "trend": "1857.9",
            "averageUnc": "1.5",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.8",
            "average": "1851.9",
            "trend": "1858.7",
            "averageUnc": "1.6",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.9",
            "average": "1860.5",
            "trend": "1859.4",
            "averageUnc": "0.9",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.10",
            "average": "1865.7",
            "trend": "1860.1",
            "averageUnc": "1.1",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.11",
            "average": "1866.2",
            "trend": "1860.9",
            "averageUnc": "1.2",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.12",
            "average": "1866.0",
            "trend": "1861.6",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2019.1",
            "average": "1865.0",
            "trend": "1862.3",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2019.2",
            "average": "1865.0",
            "trend": "1863.0",
            "averageUnc": "0.8",
            "trendUnc": "0.7"
        },
        {
            "date": "2019.3",
            "average": "1866.3",
            "trend": "1863.7",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2019.4",
            "average": "1865.3",
            "trend": "1864.4",
            "averageUnc": "0.6",
            "trendUnc": "0.6"
        },
        {
            "date": "2019.5",
            "average": "1861.9",
            "trend": "1865.1",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2019.6",
            "average": "1858.8",
            "trend": "1865.9",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2019.7",
            "average": "1858.4",
            "trend": "1866.7",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2019.8",
            "average": "1863.0",
            "trend": "1867.5",
            "averageUnc": "1.3",
            "trendUnc": "0.5"
        },
        {
            "date": "2019.9",
            "average": "1870.8",
            "trend": "1868.3",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2019.10",
            "average": "1875.4",
            "trend": "1869.2",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2019.11",
            "average": "1875.5",
            "trend": "1870.2",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2019.12",
            "average": "1874.7",
            "trend": "1871.2",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.1",
            "average": "1873.2",
            "trend": "1872.2",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.2",
            "average": "1872.7",
            "trend": "1873.3",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.3",
            "average": "1874.8",
            "trend": "1874.4",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.4",
            "average": "1875.9",
            "trend": "1875.5",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.5",
            "average": "1874.3",
            "trend": "1876.7",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.6",
            "average": "1871.9",
            "trend": "1878.0",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.7",
            "average": "1871.5",
            "trend": "1879.2",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.8",
            "average": "1876.5",
            "trend": "1880.5",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.9",
            "average": "1884.7",
            "trend": "1881.9",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.10",
            "average": "1890.1",
            "trend": "1883.2",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.11",
            "average": "1891.8",
            "trend": "1884.6",
            "averageUnc": "0.6",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.12",
            "average": "1892.2",
            "trend": "1886.1",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2021.1",
            "average": "1890.4",
            "trend": "1887.6",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2021.2",
            "average": "1888.0",
            "trend": "1889.1",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.3",
            "average": "1888.8",
            "trend": "1890.6",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.4",
            "average": "1891.2",
            "trend": "1892.1",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.5",
            "average": "1891.6",
            "trend": "1893.8",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.6",
            "average": "1888.6",
            "trend": "1895.4",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.7",
            "average": "1886.5",
            "trend": "1897.0",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.8",
            "average": "1892.7",
            "trend": "1898.6",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.9",
            "average": "1902.7",
            "trend": "1900.2",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.10",
            "average": "1908.0",
            "trend": "1901.7",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.11",
            "average": "1909.5",
            "trend": "1903.2",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.12",
            "average": "1909.6",
            "trend": "1904.5",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2022.1",
            "average": "1908.7",
            "trend": "1905.8",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2022.2",
            "average": "1908.5",
            "trend": "1906.9",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2022.3",
            "average": "1909.2",
            "trend": "1907.8",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        }
    ]
}
    return data

#create newsomething
@app.route('/thought/new')
def thought():
    return render_template('thought_new.html', data = api_thought())


#action to create in database
@app.route('/thought/create', methods = ['POST'])
def thought_create():
    #validations
    if not model_thought.Thought.validator(request.form):
        return redirect('/thought/new')
    #create thought
    data = {
        **request.form,
        'user_id': session['uuid']
    }
    model_thought.Thought.create(data)
    return redirect('/')


#calling and displaying info 
@app.route('/thought/<int:id>')
def thought_show(id):
    # id to show session id name
    data = {
        'id': id
    }
    thought = model_thought.Thought.get_one(data)
    user = model_user.User.get_one({'id':session['uuid']})
    return render_template('thought_show.html', thought = thought, user = user, data = api_thought_show())

#to show the table in  show method
@app.route('/api/thought/<int:id>')
def api_thought_show():
    data = {
    "methane": [
        {
            "date": "1983.7",
            "average": "1626.0",
            "trend": "1635.6",
            "averageUnc": "2.3",
            "trendUnc": "1.5"
        },
        {
            "date": "1983.8",
            "average": "1628.0",
            "trend": "1636.0",
            "averageUnc": "2.9",
            "trendUnc": "1.4"
        },
        {
            "date": "1983.9",
            "average": "1638.5",
            "trend": "1636.5",
            "averageUnc": "2.3",
            "trendUnc": "1.3"
        },
        {
            "date": "1983.10",
            "average": "1644.8",
            "trend": "1637.1",
            "averageUnc": "1.4",
            "trendUnc": "1.2"
        },
        {
            "date": "1983.11",
            "average": "1642.6",
            "trend": "1637.7",
            "averageUnc": "0.8",
            "trendUnc": "1.2"
        },
        {
            "date": "1983.12",
            "average": "1639.5",
            "trend": "1638.3",
            "averageUnc": "1.0",
            "trendUnc": "1.1"
        },
        {
            "date": "1984.1",
            "average": "1638.7",
            "trend": "1639.1",
            "averageUnc": "1.9",
            "trendUnc": "1.0"
        },
        {
            "date": "1984.2",
            "average": "1638.8",
            "trend": "1639.9",
            "averageUnc": "2.1",
            "trendUnc": "0.9"
        },
        {
            "date": "1984.3",
            "average": "1640.8",
            "trend": "1640.8",
            "averageUnc": "1.5",
            "trendUnc": "0.8"
        },
        {
            "date": "1984.4",
            "average": "1643.7",
            "trend": "1641.8",
            "averageUnc": "1.9",
            "trendUnc": "0.7"
        },
        {
            "date": "1984.5",
            "average": "1642.9",
            "trend": "1642.9",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "1984.6",
            "average": "1639.6",
            "trend": "1644.0",
            "averageUnc": "0.8",
            "trendUnc": "0.7"
        },
        {
            "date": "1984.7",
            "average": "1637.8",
            "trend": "1645.2",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1984.8",
            "average": "1641.3",
            "trend": "1646.4",
            "averageUnc": "1.4",
            "trendUnc": "0.6"
        },
        {
            "date": "1984.9",
            "average": "1650.4",
            "trend": "1647.5",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1984.10",
            "average": "1654.5",
            "trend": "1648.7",
            "averageUnc": "1.4",
            "trendUnc": "0.6"
        },
        {
            "date": "1984.11",
            "average": "1653.7",
            "trend": "1649.8",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1984.12",
            "average": "1656.1",
            "trend": "1651.0",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "1985.1",
            "average": "1655.6",
            "trend": "1652.1",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "1985.2",
            "average": "1652.2",
            "trend": "1653.1",
            "averageUnc": "1.5",
            "trendUnc": "0.6"
        },
        {
            "date": "1985.3",
            "average": "1654.6",
            "trend": "1654.1",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1985.4",
            "average": "1658.2",
            "trend": "1655.2",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1985.5",
            "average": "1655.9",
            "trend": "1656.2",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "1985.6",
            "average": "1650.1",
            "trend": "1657.2",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "1985.7",
            "average": "1646.8",
            "trend": "1658.2",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "1985.8",
            "average": "1652.2",
            "trend": "1659.2",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "1985.9",
            "average": "1662.5",
            "trend": "1660.2",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "1985.10",
            "average": "1667.5",
            "trend": "1661.2",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1985.11",
            "average": "1666.8",
            "trend": "1662.2",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1985.12",
            "average": "1666.1",
            "trend": "1663.3",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1986.1",
            "average": "1666.2",
            "trend": "1664.3",
            "averageUnc": "1.2",
            "trendUnc": "0.7"
        },
        {
            "date": "1986.2",
            "average": "1666.9",
            "trend": "1665.3",
            "averageUnc": "2.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1986.3",
            "average": "1669.3",
            "trend": "1666.4",
            "averageUnc": "1.5",
            "trendUnc": "0.7"
        },
        {
            "date": "1986.4",
            "average": "1670.8",
            "trend": "1667.4",
            "averageUnc": "1.5",
            "trendUnc": "0.8"
        },
        {
            "date": "1986.5",
            "average": "1668.4",
            "trend": "1668.5",
            "averageUnc": "0.9",
            "trendUnc": "0.8"
        },
        {
            "date": "1986.6",
            "average": "1664.8",
            "trend": "1669.6",
            "averageUnc": "1.3",
            "trendUnc": "0.8"
        },
        {
            "date": "1986.7",
            "average": "1662.3",
            "trend": "1670.7",
            "averageUnc": "1.2",
            "trendUnc": "0.8"
        },
        {
            "date": "1986.8",
            "average": "1664.3",
            "trend": "1671.8",
            "averageUnc": "1.6",
            "trendUnc": "0.8"
        },
        {
            "date": "1986.9",
            "average": "1672.6",
            "trend": "1672.9",
            "averageUnc": "1.5",
            "trendUnc": "0.8"
        },
        {
            "date": "1986.10",
            "average": "1678.7",
            "trend": "1674.0",
            "averageUnc": "1.5",
            "trendUnc": "0.8"
        },
        {
            "date": "1986.11",
            "average": "1679.0",
            "trend": "1675.1",
            "averageUnc": "1.7",
            "trendUnc": "0.8"
        },
        {
            "date": "1986.12",
            "average": "1679.1",
            "trend": "1676.2",
            "averageUnc": "1.2",
            "trendUnc": "0.8"
        },
        {
            "date": "1987.1",
            "average": "1679.3",
            "trend": "1677.3",
            "averageUnc": "1.2",
            "trendUnc": "0.8"
        },
        {
            "date": "1987.2",
            "average": "1679.0",
            "trend": "1678.3",
            "averageUnc": "1.1",
            "trendUnc": "0.8"
        },
        {
            "date": "1987.3",
            "average": "1680.1",
            "trend": "1679.3",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "1987.4",
            "average": "1681.4",
            "trend": "1680.4",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1987.5",
            "average": "1681.9",
            "trend": "1681.4",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1987.6",
            "average": "1680.0",
            "trend": "1682.4",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1987.7",
            "average": "1676.0",
            "trend": "1683.3",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1987.8",
            "average": "1677.1",
            "trend": "1684.3",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1987.9",
            "average": "1685.6",
            "trend": "1685.2",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "1987.10",
            "average": "1691.6",
            "trend": "1686.0",
            "averageUnc": "1.1",
            "trendUnc": "0.4"
        },
        {
            "date": "1987.11",
            "average": "1691.1",
            "trend": "1686.9",
            "averageUnc": "0.8",
            "trendUnc": "0.4"
        },
        {
            "date": "1987.12",
            "average": "1690.5",
            "trend": "1687.7",
            "averageUnc": "0.9",
            "trendUnc": "0.4"
        },
        {
            "date": "1988.1",
            "average": "1691.9",
            "trend": "1688.5",
            "averageUnc": "0.7",
            "trendUnc": "0.4"
        },
        {
            "date": "1988.2",
            "average": "1692.5",
            "trend": "1689.3",
            "averageUnc": "0.8",
            "trendUnc": "0.4"
        },
        {
            "date": "1988.3",
            "average": "1691.3",
            "trend": "1690.1",
            "averageUnc": "1.0",
            "trendUnc": "0.4"
        },
        {
            "date": "1988.4",
            "average": "1690.0",
            "trend": "1690.9",
            "averageUnc": "0.9",
            "trendUnc": "0.4"
        },
        {
            "date": "1988.5",
            "average": "1689.0",
            "trend": "1691.8",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1988.6",
            "average": "1687.1",
            "trend": "1692.7",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "1988.7",
            "average": "1685.9",
            "trend": "1693.5",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1988.8",
            "average": "1689.3",
            "trend": "1694.5",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1988.9",
            "average": "1696.3",
            "trend": "1695.4",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1988.10",
            "average": "1701.3",
            "trend": "1696.4",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1988.11",
            "average": "1702.9",
            "trend": "1697.4",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "1988.12",
            "average": "1702.0",
            "trend": "1698.4",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1989.1",
            "average": "1700.6",
            "trend": "1699.4",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1989.2",
            "average": "1701.1",
            "trend": "1700.4",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1989.3",
            "average": "1702.5",
            "trend": "1701.4",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1989.4",
            "average": "1703.7",
            "trend": "1702.4",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1989.5",
            "average": "1703.4",
            "trend": "1703.4",
            "averageUnc": "0.6",
            "trendUnc": "0.6"
        },
        {
            "date": "1989.6",
            "average": "1700.3",
            "trend": "1704.4",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1989.7",
            "average": "1698.2",
            "trend": "1705.3",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1989.8",
            "average": "1702.0",
            "trend": "1706.2",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1989.9",
            "average": "1707.2",
            "trend": "1707.1",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1989.10",
            "average": "1710.5",
            "trend": "1708.0",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "1989.11",
            "average": "1713.1",
            "trend": "1708.8",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1989.12",
            "average": "1713.2",
            "trend": "1709.6",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1990.1",
            "average": "1712.0",
            "trend": "1710.4",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1990.2",
            "average": "1713.3",
            "trend": "1711.1",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1990.3",
            "average": "1714.4",
            "trend": "1711.7",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "1990.4",
            "average": "1712.6",
            "trend": "1712.4",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "1990.5",
            "average": "1710.7",
            "trend": "1713.1",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "1990.6",
            "average": "1708.3",
            "trend": "1713.8",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "1990.7",
            "average": "1706.4",
            "trend": "1714.4",
            "averageUnc": "0.8",
            "trendUnc": "0.7"
        },
        {
            "date": "1990.8",
            "average": "1710.1",
            "trend": "1715.1",
            "averageUnc": "1.2",
            "trendUnc": "0.7"
        },
        {
            "date": "1990.9",
            "average": "1717.6",
            "trend": "1715.8",
            "averageUnc": "1.2",
            "trendUnc": "0.7"
        },
        {
            "date": "1990.10",
            "average": "1722.0",
            "trend": "1716.6",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "1990.11",
            "average": "1723.5",
            "trend": "1717.4",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1990.12",
            "average": "1723.4",
            "trend": "1718.2",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1991.1",
            "average": "1721.6",
            "trend": "1719.2",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1991.2",
            "average": "1721.2",
            "trend": "1720.2",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "1991.3",
            "average": "1722.1",
            "trend": "1721.2",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1991.4",
            "average": "1722.5",
            "trend": "1722.4",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1991.5",
            "average": "1722.2",
            "trend": "1723.6",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1991.6",
            "average": "1719.0",
            "trend": "1724.9",
            "averageUnc": "1.2",
            "trendUnc": "0.7"
        },
        {
            "date": "1991.7",
            "average": "1716.1",
            "trend": "1726.2",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1991.8",
            "average": "1719.2",
            "trend": "1727.5",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "1991.9",
            "average": "1726.2",
            "trend": "1728.8",
            "averageUnc": "1.3",
            "trendUnc": "0.7"
        },
        {
            "date": "1991.10",
            "average": "1732.7",
            "trend": "1730.1",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1991.11",
            "average": "1737.5",
            "trend": "1731.2",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "1991.12",
            "average": "1739.7",
            "trend": "1732.3",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "1992.1",
            "average": "1738.9",
            "trend": "1733.2",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "1992.2",
            "average": "1737.3",
            "trend": "1734.0",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "1992.3",
            "average": "1737.0",
            "trend": "1734.6",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1992.4",
            "average": "1736.6",
            "trend": "1735.1",
            "averageUnc": "0.6",
            "trendUnc": "0.6"
        },
        {
            "date": "1992.5",
            "average": "1734.9",
            "trend": "1735.4",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "1992.6",
            "average": "1731.6",
            "trend": "1735.6",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1992.7",
            "average": "1728.9",
            "trend": "1735.7",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1992.8",
            "average": "1730.4",
            "trend": "1735.7",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1992.9",
            "average": "1734.7",
            "trend": "1735.6",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1992.10",
            "average": "1737.8",
            "trend": "1735.4",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1992.11",
            "average": "1739.3",
            "trend": "1735.3",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "1992.12",
            "average": "1738.6",
            "trend": "1735.2",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1993.1",
            "average": "1735.8",
            "trend": "1735.1",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1993.2",
            "average": "1734.4",
            "trend": "1735.1",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "1993.3",
            "average": "1735.5",
            "trend": "1735.2",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1993.4",
            "average": "1736.7",
            "trend": "1735.3",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1993.5",
            "average": "1735.0",
            "trend": "1735.5",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1993.6",
            "average": "1730.9",
            "trend": "1735.8",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1993.7",
            "average": "1728.0",
            "trend": "1736.2",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1993.8",
            "average": "1731.2",
            "trend": "1736.6",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1993.9",
            "average": "1738.5",
            "trend": "1737.1",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1993.10",
            "average": "1743.3",
            "trend": "1737.6",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1993.11",
            "average": "1745.2",
            "trend": "1738.1",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "1993.12",
            "average": "1744.3",
            "trend": "1738.7",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.1",
            "average": "1741.4",
            "trend": "1739.3",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.2",
            "average": "1740.9",
            "trend": "1739.8",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.3",
            "average": "1741.9",
            "trend": "1740.4",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.4",
            "average": "1741.9",
            "trend": "1741.0",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.5",
            "average": "1740.6",
            "trend": "1741.6",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.6",
            "average": "1736.9",
            "trend": "1742.2",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.7",
            "average": "1732.4",
            "trend": "1742.9",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.8",
            "average": "1734.1",
            "trend": "1743.5",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.9",
            "average": "1743.0",
            "trend": "1744.1",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.10",
            "average": "1749.8",
            "trend": "1744.7",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.11",
            "average": "1751.2",
            "trend": "1745.3",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.12",
            "average": "1751.6",
            "trend": "1745.9",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1995.1",
            "average": "1751.0",
            "trend": "1746.5",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1995.2",
            "average": "1749.4",
            "trend": "1747.0",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1995.3",
            "average": "1748.9",
            "trend": "1747.5",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "1995.4",
            "average": "1749.4",
            "trend": "1747.9",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "1995.5",
            "average": "1747.7",
            "trend": "1748.3",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "1995.6",
            "average": "1742.8",
            "trend": "1748.7",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1995.7",
            "average": "1740.1",
            "trend": "1749.0",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1995.8",
            "average": "1743.5",
            "trend": "1749.2",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "1995.9",
            "average": "1749.7",
            "trend": "1749.5",
            "averageUnc": "1.3",
            "trendUnc": "0.5"
        },
        {
            "date": "1995.10",
            "average": "1754.2",
            "trend": "1749.7",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1995.11",
            "average": "1755.3",
            "trend": "1749.9",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1995.12",
            "average": "1753.7",
            "trend": "1750.1",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1996.1",
            "average": "1752.3",
            "trend": "1750.2",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1996.2",
            "average": "1752.9",
            "trend": "1750.4",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1996.3",
            "average": "1752.4",
            "trend": "1750.6",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1996.4",
            "average": "1749.9",
            "trend": "1750.8",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1996.5",
            "average": "1748.6",
            "trend": "1751.0",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "1996.6",
            "average": "1746.2",
            "trend": "1751.2",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1996.7",
            "average": "1742.2",
            "trend": "1751.4",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "1996.8",
            "average": "1744.7",
            "trend": "1751.7",
            "averageUnc": "1.3",
            "trendUnc": "0.7"
        },
        {
            "date": "1996.9",
            "average": "1753.0",
            "trend": "1751.9",
            "averageUnc": "1.3",
            "trendUnc": "0.7"
        },
        {
            "date": "1996.10",
            "average": "1759.0",
            "trend": "1752.1",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1996.11",
            "average": "1759.9",
            "trend": "1752.3",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1996.12",
            "average": "1756.8",
            "trend": "1752.5",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "1997.1",
            "average": "1753.4",
            "trend": "1752.8",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1997.2",
            "average": "1753.8",
            "trend": "1753.0",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1997.3",
            "average": "1755.6",
            "trend": "1753.2",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1997.4",
            "average": "1755.5",
            "trend": "1753.5",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1997.5",
            "average": "1753.9",
            "trend": "1753.9",
            "averageUnc": "0.7",
            "trendUnc": "0.4"
        },
        {
            "date": "1997.6",
            "average": "1750.2",
            "trend": "1754.2",
            "averageUnc": "0.9",
            "trendUnc": "0.4"
        },
        {
            "date": "1997.7",
            "average": "1746.2",
            "trend": "1754.7",
            "averageUnc": "1.0",
            "trendUnc": "0.4"
        },
        {
            "date": "1997.8",
            "average": "1747.9",
            "trend": "1755.3",
            "averageUnc": "0.9",
            "trendUnc": "0.4"
        },
        {
            "date": "1997.9",
            "average": "1755.1",
            "trend": "1755.9",
            "averageUnc": "0.9",
            "trendUnc": "0.4"
        },
        {
            "date": "1997.10",
            "average": "1760.2",
            "trend": "1756.6",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1997.11",
            "average": "1761.7",
            "trend": "1757.5",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1997.12",
            "average": "1761.9",
            "trend": "1758.4",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1998.1",
            "average": "1761.5",
            "trend": "1759.4",
            "averageUnc": "0.7",
            "trendUnc": "0.5"
        },
        {
            "date": "1998.2",
            "average": "1761.5",
            "trend": "1760.5",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "1998.3",
            "average": "1763.0",
            "trend": "1761.6",
            "averageUnc": "1.6",
            "trendUnc": "0.6"
        },
        {
            "date": "1998.4",
            "average": "1764.7",
            "trend": "1762.8",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "1998.5",
            "average": "1764.2",
            "trend": "1764.0",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1998.6",
            "average": "1760.3",
            "trend": "1765.1",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "1998.7",
            "average": "1756.1",
            "trend": "1766.3",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1998.8",
            "average": "1760.1",
            "trend": "1767.4",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1998.9",
            "average": "1770.5",
            "trend": "1768.4",
            "averageUnc": "1.3",
            "trendUnc": "0.7"
        },
        {
            "date": "1998.10",
            "average": "1776.2",
            "trend": "1769.3",
            "averageUnc": "1.3",
            "trendUnc": "0.7"
        },
        {
            "date": "1998.11",
            "average": "1775.6",
            "trend": "1770.1",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "1998.12",
            "average": "1774.2",
            "trend": "1770.7",
            "averageUnc": "0.8",
            "trendUnc": "0.7"
        },
        {
            "date": "1999.1",
            "average": "1774.0",
            "trend": "1771.3",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1999.2",
            "average": "1774.2",
            "trend": "1771.8",
            "averageUnc": "1.5",
            "trendUnc": "0.7"
        },
        {
            "date": "1999.3",
            "average": "1774.7",
            "trend": "1772.2",
            "averageUnc": "1.2",
            "trendUnc": "0.7"
        },
        {
            "date": "1999.4",
            "average": "1774.9",
            "trend": "1772.5",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "1999.5",
            "average": "1772.7",
            "trend": "1772.8",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1999.6",
            "average": "1767.4",
            "trend": "1773.0",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "1999.7",
            "average": "1763.0",
            "trend": "1773.1",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "1999.8",
            "average": "1764.7",
            "trend": "1773.2",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1999.9",
            "average": "1771.1",
            "trend": "1773.3",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "1999.10",
            "average": "1776.6",
            "trend": "1773.4",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "1999.11",
            "average": "1778.6",
            "trend": "1773.4",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "1999.12",
            "average": "1777.3",
            "trend": "1773.4",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2000.1",
            "average": "1775.7",
            "trend": "1773.5",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2000.2",
            "average": "1775.8",
            "trend": "1773.5",
            "averageUnc": "1.4",
            "trendUnc": "0.7"
        },
        {
            "date": "2000.3",
            "average": "1776.9",
            "trend": "1773.4",
            "averageUnc": "1.5",
            "trendUnc": "0.7"
        },
        {
            "date": "2000.4",
            "average": "1777.4",
            "trend": "1773.4",
            "averageUnc": "1.4",
            "trendUnc": "0.7"
        },
        {
            "date": "2000.5",
            "average": "1774.6",
            "trend": "1773.3",
            "averageUnc": "1.2",
            "trendUnc": "0.8"
        },
        {
            "date": "2000.6",
            "average": "1768.2",
            "trend": "1773.2",
            "averageUnc": "1.1",
            "trendUnc": "0.8"
        },
        {
            "date": "2000.7",
            "average": "1763.6",
            "trend": "1773.1",
            "averageUnc": "0.8",
            "trendUnc": "0.8"
        },
        {
            "date": "2000.8",
            "average": "1765.7",
            "trend": "1772.9",
            "averageUnc": "1.0",
            "trendUnc": "0.8"
        },
        {
            "date": "2000.9",
            "average": "1772.2",
            "trend": "1772.7",
            "averageUnc": "1.1",
            "trendUnc": "0.8"
        },
        {
            "date": "2000.10",
            "average": "1777.1",
            "trend": "1772.5",
            "averageUnc": "0.8",
            "trendUnc": "0.7"
        },
        {
            "date": "2000.11",
            "average": "1777.7",
            "trend": "1772.3",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2000.12",
            "average": "1775.3",
            "trend": "1772.1",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2001.1",
            "average": "1772.9",
            "trend": "1771.9",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "2001.2",
            "average": "1772.5",
            "trend": "1771.7",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2001.3",
            "average": "1773.7",
            "trend": "1771.5",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2001.4",
            "average": "1773.9",
            "trend": "1771.3",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "2001.5",
            "average": "1770.8",
            "trend": "1771.2",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2001.6",
            "average": "1765.9",
            "trend": "1771.1",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2001.7",
            "average": "1762.8",
            "trend": "1771.1",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2001.8",
            "average": "1764.3",
            "trend": "1771.0",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2001.9",
            "average": "1770.5",
            "trend": "1771.0",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "2001.10",
            "average": "1775.5",
            "trend": "1771.1",
            "averageUnc": "0.6",
            "trendUnc": "0.5"
        },
        {
            "date": "2001.11",
            "average": "1776.6",
            "trend": "1771.1",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "2001.12",
            "average": "1775.9",
            "trend": "1771.2",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2002.1",
            "average": "1774.1",
            "trend": "1771.3",
            "averageUnc": "1.2",
            "trendUnc": "0.4"
        },
        {
            "date": "2002.2",
            "average": "1772.8",
            "trend": "1771.4",
            "averageUnc": "1.0",
            "trendUnc": "0.4"
        },
        {
            "date": "2002.3",
            "average": "1773.4",
            "trend": "1771.6",
            "averageUnc": "0.6",
            "trendUnc": "0.4"
        },
        {
            "date": "2002.4",
            "average": "1772.7",
            "trend": "1771.7",
            "averageUnc": "0.6",
            "trendUnc": "0.4"
        },
        {
            "date": "2002.5",
            "average": "1770.3",
            "trend": "1771.9",
            "averageUnc": "0.7",
            "trendUnc": "0.5"
        },
        {
            "date": "2002.6",
            "average": "1766.9",
            "trend": "1772.1",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "2002.7",
            "average": "1764.3",
            "trend": "1772.4",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2002.8",
            "average": "1767.0",
            "trend": "1772.7",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2002.9",
            "average": "1773.8",
            "trend": "1773.0",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2002.10",
            "average": "1778.2",
            "trend": "1773.4",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2002.11",
            "average": "1779.6",
            "trend": "1773.8",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2002.12",
            "average": "1779.7",
            "trend": "1774.2",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2003.1",
            "average": "1777.5",
            "trend": "1774.8",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2003.2",
            "average": "1774.8",
            "trend": "1775.3",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2003.3",
            "average": "1774.8",
            "trend": "1775.8",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2003.4",
            "average": "1775.7",
            "trend": "1776.4",
            "averageUnc": "1.3",
            "trendUnc": "0.5"
        },
        {
            "date": "2003.5",
            "average": "1774.4",
            "trend": "1777.0",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2003.6",
            "average": "1771.7",
            "trend": "1777.5",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "2003.7",
            "average": "1770.7",
            "trend": "1778.0",
            "averageUnc": "1.8",
            "trendUnc": "0.5"
        },
        {
            "date": "2003.8",
            "average": "1774.2",
            "trend": "1778.5",
            "averageUnc": "1.6",
            "trendUnc": "0.5"
        },
        {
            "date": "2003.9",
            "average": "1780.5",
            "trend": "1778.8",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2003.10",
            "average": "1784.7",
            "trend": "1779.1",
            "averageUnc": "0.7",
            "trendUnc": "0.5"
        },
        {
            "date": "2003.11",
            "average": "1785.3",
            "trend": "1779.3",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2003.12",
            "average": "1783.6",
            "trend": "1779.3",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2004.1",
            "average": "1780.9",
            "trend": "1779.2",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2004.2",
            "average": "1779.9",
            "trend": "1779.1",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2004.3",
            "average": "1781.0",
            "trend": "1778.8",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2004.4",
            "average": "1780.7",
            "trend": "1778.4",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2004.5",
            "average": "1777.6",
            "trend": "1777.9",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2004.6",
            "average": "1772.3",
            "trend": "1777.4",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2004.7",
            "average": "1768.0",
            "trend": "1776.9",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2004.8",
            "average": "1769.7",
            "trend": "1776.3",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2004.9",
            "average": "1775.5",
            "trend": "1775.8",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2004.10",
            "average": "1779.7",
            "trend": "1775.3",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2004.11",
            "average": "1780.5",
            "trend": "1774.9",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2004.12",
            "average": "1778.3",
            "trend": "1774.6",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.1",
            "average": "1776.0",
            "trend": "1774.3",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.2",
            "average": "1775.6",
            "trend": "1774.1",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.3",
            "average": "1775.5",
            "trend": "1774.1",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.4",
            "average": "1774.6",
            "trend": "1774.0",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.5",
            "average": "1772.3",
            "trend": "1774.1",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.6",
            "average": "1768.7",
            "trend": "1774.2",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.7",
            "average": "1766.3",
            "trend": "1774.3",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.8",
            "average": "1768.0",
            "trend": "1774.4",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.9",
            "average": "1773.2",
            "trend": "1774.5",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.10",
            "average": "1778.6",
            "trend": "1774.6",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.11",
            "average": "1781.1",
            "trend": "1774.7",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.12",
            "average": "1780.1",
            "trend": "1774.8",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2006.1",
            "average": "1779.4",
            "trend": "1774.8",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2006.2",
            "average": "1779.4",
            "trend": "1774.8",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2006.3",
            "average": "1777.4",
            "trend": "1774.7",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "2006.4",
            "average": "1776.1",
            "trend": "1774.7",
            "averageUnc": "0.7",
            "trendUnc": "0.5"
        },
        {
            "date": "2006.5",
            "average": "1775.0",
            "trend": "1774.7",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2006.6",
            "average": "1769.3",
            "trend": "1774.7",
            "averageUnc": "1.3",
            "trendUnc": "0.5"
        },
        {
            "date": "2006.7",
            "average": "1764.2",
            "trend": "1774.8",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "2006.8",
            "average": "1767.2",
            "trend": "1774.9",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "2006.9",
            "average": "1774.6",
            "trend": "1775.2",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2006.10",
            "average": "1778.2",
            "trend": "1775.5",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2006.11",
            "average": "1779.0",
            "trend": "1775.9",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "2006.12",
            "average": "1779.9",
            "trend": "1776.4",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.1",
            "average": "1779.2",
            "trend": "1777.0",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.2",
            "average": "1778.7",
            "trend": "1777.6",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.3",
            "average": "1780.3",
            "trend": "1778.3",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.4",
            "average": "1781.1",
            "trend": "1779.0",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.5",
            "average": "1779.4",
            "trend": "1779.8",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.6",
            "average": "1775.6",
            "trend": "1780.5",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.7",
            "average": "1772.6",
            "trend": "1781.2",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.8",
            "average": "1777.2",
            "trend": "1781.9",
            "averageUnc": "1.5",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.9",
            "average": "1785.9",
            "trend": "1782.6",
            "averageUnc": "1.5",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.10",
            "average": "1789.9",
            "trend": "1783.2",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.11",
            "average": "1789.5",
            "trend": "1783.7",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2007.12",
            "average": "1788.2",
            "trend": "1784.3",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.1",
            "average": "1786.8",
            "trend": "1784.8",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.2",
            "average": "1785.8",
            "trend": "1785.3",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.3",
            "average": "1786.1",
            "trend": "1785.8",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.4",
            "average": "1786.8",
            "trend": "1786.3",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.5",
            "average": "1785.1",
            "trend": "1786.8",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.6",
            "average": "1780.4",
            "trend": "1787.3",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.7",
            "average": "1777.6",
            "trend": "1787.9",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.8",
            "average": "1781.0",
            "trend": "1788.5",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.9",
            "average": "1787.7",
            "trend": "1789.0",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.10",
            "average": "1793.7",
            "trend": "1789.6",
            "averageUnc": "0.7",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.11",
            "average": "1797.4",
            "trend": "1790.2",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.12",
            "average": "1796.7",
            "trend": "1790.8",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2009.1",
            "average": "1795.1",
            "trend": "1791.4",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2009.2",
            "average": "1795.6",
            "trend": "1791.9",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "2009.3",
            "average": "1796.1",
            "trend": "1792.3",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2009.4",
            "average": "1795.6",
            "trend": "1792.8",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2009.5",
            "average": "1792.3",
            "trend": "1793.2",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "2009.6",
            "average": "1786.9",
            "trend": "1793.6",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2009.7",
            "average": "1784.9",
            "trend": "1794.0",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "2009.8",
            "average": "1788.8",
            "trend": "1794.3",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2009.9",
            "average": "1794.8",
            "trend": "1794.6",
            "averageUnc": "1.2",
            "trendUnc": "0.7"
        },
        {
            "date": "2009.10",
            "average": "1798.0",
            "trend": "1794.9",
            "averageUnc": "1.4",
            "trendUnc": "0.7"
        },
        {
            "date": "2009.11",
            "average": "1797.9",
            "trend": "1795.2",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2009.12",
            "average": "1796.7",
            "trend": "1795.6",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.1",
            "average": "1797.1",
            "trend": "1795.9",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.2",
            "average": "1798.7",
            "trend": "1796.3",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.3",
            "average": "1799.4",
            "trend": "1796.7",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.4",
            "average": "1799.6",
            "trend": "1797.1",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.5",
            "average": "1797.7",
            "trend": "1797.5",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.6",
            "average": "1792.6",
            "trend": "1797.9",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.7",
            "average": "1789.4",
            "trend": "1798.4",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.8",
            "average": "1794.0",
            "trend": "1798.9",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.9",
            "average": "1801.8",
            "trend": "1799.3",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.10",
            "average": "1806.5",
            "trend": "1799.8",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.11",
            "average": "1807.0",
            "trend": "1800.3",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2010.12",
            "average": "1803.6",
            "trend": "1800.7",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.1",
            "average": "1800.5",
            "trend": "1801.2",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.2",
            "average": "1800.2",
            "trend": "1801.6",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.3",
            "average": "1801.0",
            "trend": "1802.0",
            "averageUnc": "0.7",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.4",
            "average": "1802.9",
            "trend": "1802.4",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.5",
            "average": "1803.3",
            "trend": "1802.8",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.6",
            "average": "1799.2",
            "trend": "1803.2",
            "averageUnc": "0.7",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.7",
            "average": "1796.1",
            "trend": "1803.6",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.8",
            "average": "1798.9",
            "trend": "1804.0",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.9",
            "average": "1804.0",
            "trend": "1804.4",
            "averageUnc": "1.6",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.10",
            "average": "1809.5",
            "trend": "1804.8",
            "averageUnc": "1.6",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.11",
            "average": "1812.3",
            "trend": "1805.2",
            "averageUnc": "1.3",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.12",
            "average": "1810.0",
            "trend": "1805.6",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2012.1",
            "average": "1807.3",
            "trend": "1806.0",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2012.2",
            "average": "1808.3",
            "trend": "1806.4",
            "averageUnc": "1.4",
            "trendUnc": "0.7"
        },
        {
            "date": "2012.3",
            "average": "1810.0",
            "trend": "1806.9",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2012.4",
            "average": "1808.4",
            "trend": "1807.3",
            "averageUnc": "0.6",
            "trendUnc": "0.7"
        },
        {
            "date": "2012.5",
            "average": "1804.7",
            "trend": "1807.8",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2012.6",
            "average": "1800.9",
            "trend": "1808.2",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2012.7",
            "average": "1799.2",
            "trend": "1808.6",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2012.8",
            "average": "1803.2",
            "trend": "1809.1",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2012.9",
            "average": "1810.1",
            "trend": "1809.5",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2012.10",
            "average": "1814.7",
            "trend": "1809.9",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2012.11",
            "average": "1815.9",
            "trend": "1810.3",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2012.12",
            "average": "1814.6",
            "trend": "1810.6",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.1",
            "average": "1814.1",
            "trend": "1811.0",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.2",
            "average": "1814.2",
            "trend": "1811.3",
            "averageUnc": "1.6",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.3",
            "average": "1813.3",
            "trend": "1811.6",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.4",
            "average": "1812.8",
            "trend": "1812.0",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.5",
            "average": "1811.9",
            "trend": "1812.3",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.6",
            "average": "1808.5",
            "trend": "1812.7",
            "averageUnc": "1.4",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.7",
            "average": "1805.7",
            "trend": "1813.1",
            "averageUnc": "1.5",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.8",
            "average": "1808.4",
            "trend": "1813.6",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.9",
            "average": "1814.3",
            "trend": "1814.1",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.10",
            "average": "1818.6",
            "trend": "1814.7",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.11",
            "average": "1820.4",
            "trend": "1815.4",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.12",
            "average": "1819.4",
            "trend": "1816.1",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2014.1",
            "average": "1816.9",
            "trend": "1817.0",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2014.2",
            "average": "1816.4",
            "trend": "1817.9",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2014.3",
            "average": "1818.1",
            "trend": "1818.8",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "2014.4",
            "average": "1820.9",
            "trend": "1819.9",
            "averageUnc": "0.6",
            "trendUnc": "0.5"
        },
        {
            "date": "2014.5",
            "average": "1821.9",
            "trend": "1820.9",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "2014.6",
            "average": "1818.4",
            "trend": "1822.1",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "2014.7",
            "average": "1815.6",
            "trend": "1823.2",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2014.8",
            "average": "1819.8",
            "trend": "1824.4",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2014.9",
            "average": "1827.0",
            "trend": "1825.5",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2014.10",
            "average": "1831.3",
            "trend": "1826.6",
            "averageUnc": "0.6",
            "trendUnc": "0.5"
        },
        {
            "date": "2014.11",
            "average": "1833.1",
            "trend": "1827.7",
            "averageUnc": "0.6",
            "trendUnc": "0.5"
        },
        {
            "date": "2014.12",
            "average": "1833.5",
            "trend": "1828.8",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "2015.1",
            "average": "1832.9",
            "trend": "1829.8",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2015.2",
            "average": "1832.7",
            "trend": "1830.7",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "2015.3",
            "average": "1833.1",
            "trend": "1831.6",
            "averageUnc": "0.7",
            "trendUnc": "0.5"
        },
        {
            "date": "2015.4",
            "average": "1833.2",
            "trend": "1832.5",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2015.5",
            "average": "1831.8",
            "trend": "1833.4",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2015.6",
            "average": "1827.4",
            "trend": "1834.2",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2015.7",
            "average": "1824.8",
            "trend": "1835.0",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2015.8",
            "average": "1829.2",
            "trend": "1835.8",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2015.9",
            "average": "1836.2",
            "trend": "1836.6",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2015.10",
            "average": "1841.5",
            "trend": "1837.4",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2015.11",
            "average": "1844.7",
            "trend": "1838.2",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2015.12",
            "average": "1844.9",
            "trend": "1838.9",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2016.1",
            "average": "1842.4",
            "trend": "1839.7",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2016.2",
            "average": "1841.6",
            "trend": "1840.4",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2016.3",
            "average": "1843.0",
            "trend": "1841.0",
            "averageUnc": "0.8",
            "trendUnc": "0.7"
        },
        {
            "date": "2016.4",
            "average": "1843.7",
            "trend": "1841.7",
            "averageUnc": "0.7",
            "trendUnc": "0.7"
        },
        {
            "date": "2016.5",
            "average": "1842.1",
            "trend": "1842.3",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2016.6",
            "average": "1837.9",
            "trend": "1843.0",
            "averageUnc": "1.2",
            "trendUnc": "0.7"
        },
        {
            "date": "2016.7",
            "average": "1834.2",
            "trend": "1843.5",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2016.8",
            "average": "1836.7",
            "trend": "1844.1",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2016.9",
            "average": "1844.2",
            "trend": "1844.6",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2016.10",
            "average": "1849.9",
            "trend": "1845.1",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2016.11",
            "average": "1851.4",
            "trend": "1845.6",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2016.12",
            "average": "1851.1",
            "trend": "1846.1",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2017.1",
            "average": "1849.8",
            "trend": "1846.6",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2017.2",
            "average": "1848.5",
            "trend": "1847.1",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2017.3",
            "average": "1848.3",
            "trend": "1847.6",
            "averageUnc": "1.4",
            "trendUnc": "0.6"
        },
        {
            "date": "2017.4",
            "average": "1848.6",
            "trend": "1848.1",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2017.5",
            "average": "1847.2",
            "trend": "1848.6",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2017.6",
            "average": "1843.0",
            "trend": "1849.2",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2017.7",
            "average": "1840.4",
            "trend": "1849.7",
            "averageUnc": "1.3",
            "trendUnc": "0.7"
        },
        {
            "date": "2017.8",
            "average": "1844.6",
            "trend": "1850.3",
            "averageUnc": "1.2",
            "trendUnc": "0.7"
        },
        {
            "date": "2017.9",
            "average": "1852.8",
            "trend": "1850.9",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "2017.10",
            "average": "1858.1",
            "trend": "1851.6",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2017.11",
            "average": "1858.7",
            "trend": "1852.2",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "2017.12",
            "average": "1856.7",
            "trend": "1852.9",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "2018.1",
            "average": "1854.5",
            "trend": "1853.6",
            "averageUnc": "1.0",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.2",
            "average": "1855.0",
            "trend": "1854.3",
            "averageUnc": "0.9",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.3",
            "average": "1856.9",
            "trend": "1855.0",
            "averageUnc": "0.9",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.4",
            "average": "1856.7",
            "trend": "1855.7",
            "averageUnc": "1.1",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.5",
            "average": "1854.8",
            "trend": "1856.4",
            "averageUnc": "1.6",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.6",
            "average": "1852.0",
            "trend": "1857.2",
            "averageUnc": "1.5",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.7",
            "average": "1849.0",
            "trend": "1857.9",
            "averageUnc": "1.5",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.8",
            "average": "1851.9",
            "trend": "1858.7",
            "averageUnc": "1.6",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.9",
            "average": "1860.5",
            "trend": "1859.4",
            "averageUnc": "0.9",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.10",
            "average": "1865.7",
            "trend": "1860.1",
            "averageUnc": "1.1",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.11",
            "average": "1866.2",
            "trend": "1860.9",
            "averageUnc": "1.2",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.12",
            "average": "1866.0",
            "trend": "1861.6",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2019.1",
            "average": "1865.0",
            "trend": "1862.3",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2019.2",
            "average": "1865.0",
            "trend": "1863.0",
            "averageUnc": "0.8",
            "trendUnc": "0.7"
        },
        {
            "date": "2019.3",
            "average": "1866.3",
            "trend": "1863.7",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2019.4",
            "average": "1865.3",
            "trend": "1864.4",
            "averageUnc": "0.6",
            "trendUnc": "0.6"
        },
        {
            "date": "2019.5",
            "average": "1861.9",
            "trend": "1865.1",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2019.6",
            "average": "1858.8",
            "trend": "1865.9",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2019.7",
            "average": "1858.4",
            "trend": "1866.7",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2019.8",
            "average": "1863.0",
            "trend": "1867.5",
            "averageUnc": "1.3",
            "trendUnc": "0.5"
        },
        {
            "date": "2019.9",
            "average": "1870.8",
            "trend": "1868.3",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2019.10",
            "average": "1875.4",
            "trend": "1869.2",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2019.11",
            "average": "1875.5",
            "trend": "1870.2",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2019.12",
            "average": "1874.7",
            "trend": "1871.2",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.1",
            "average": "1873.2",
            "trend": "1872.2",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.2",
            "average": "1872.7",
            "trend": "1873.3",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.3",
            "average": "1874.8",
            "trend": "1874.4",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.4",
            "average": "1875.9",
            "trend": "1875.5",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.5",
            "average": "1874.3",
            "trend": "1876.7",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.6",
            "average": "1871.9",
            "trend": "1878.0",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.7",
            "average": "1871.5",
            "trend": "1879.2",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.8",
            "average": "1876.5",
            "trend": "1880.5",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.9",
            "average": "1884.7",
            "trend": "1881.9",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.10",
            "average": "1890.1",
            "trend": "1883.2",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.11",
            "average": "1891.8",
            "trend": "1884.6",
            "averageUnc": "0.6",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.12",
            "average": "1892.2",
            "trend": "1886.1",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2021.1",
            "average": "1890.4",
            "trend": "1887.6",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2021.2",
            "average": "1888.0",
            "trend": "1889.1",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.3",
            "average": "1888.8",
            "trend": "1890.6",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.4",
            "average": "1891.2",
            "trend": "1892.1",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.5",
            "average": "1891.6",
            "trend": "1893.8",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.6",
            "average": "1888.6",
            "trend": "1895.4",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.7",
            "average": "1886.5",
            "trend": "1897.0",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.8",
            "average": "1892.7",
            "trend": "1898.6",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.9",
            "average": "1902.7",
            "trend": "1900.2",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.10",
            "average": "1908.0",
            "trend": "1901.7",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.11",
            "average": "1909.5",
            "trend": "1903.2",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.12",
            "average": "1909.6",
            "trend": "1904.5",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2022.1",
            "average": "1908.7",
            "trend": "1905.8",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2022.2",
            "average": "1908.5",
            "trend": "1906.9",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2022.3",
            "average": "1909.2",
            "trend": "1907.8",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        }
    ]
}
    return data

#calling page with form for modification on form
@app.route('/thought/<int:id>/edit')
def thought_edit(id):
    context = {
        'thought' :model_thought.Thought.get_one({'id': id})
    }
    return render_template('thought_edit.html', **context, data = api_thought_edit())

@app.route('/api/thought/<int:id>/edit')
def api_thought_edit():
    data = {
    "methane": [
        {
            "date": "1983.7",
            "average": "1626.0",
            "trend": "1635.6",
            "averageUnc": "2.3",
            "trendUnc": "1.5"
        },
        {
            "date": "1983.8",
            "average": "1628.0",
            "trend": "1636.0",
            "averageUnc": "2.9",
            "trendUnc": "1.4"
        },
        {
            "date": "1983.9",
            "average": "1638.5",
            "trend": "1636.5",
            "averageUnc": "2.3",
            "trendUnc": "1.3"
        },
        {
            "date": "1983.10",
            "average": "1644.8",
            "trend": "1637.1",
            "averageUnc": "1.4",
            "trendUnc": "1.2"
        },
        {
            "date": "1983.11",
            "average": "1642.6",
            "trend": "1637.7",
            "averageUnc": "0.8",
            "trendUnc": "1.2"
        },
        {
            "date": "1983.12",
            "average": "1639.5",
            "trend": "1638.3",
            "averageUnc": "1.0",
            "trendUnc": "1.1"
        },
        {
            "date": "1984.1",
            "average": "1638.7",
            "trend": "1639.1",
            "averageUnc": "1.9",
            "trendUnc": "1.0"
        },
        {
            "date": "1984.2",
            "average": "1638.8",
            "trend": "1639.9",
            "averageUnc": "2.1",
            "trendUnc": "0.9"
        },
        {
            "date": "1984.3",
            "average": "1640.8",
            "trend": "1640.8",
            "averageUnc": "1.5",
            "trendUnc": "0.8"
        },
        {
            "date": "1984.4",
            "average": "1643.7",
            "trend": "1641.8",
            "averageUnc": "1.9",
            "trendUnc": "0.7"
        },
        {
            "date": "1984.5",
            "average": "1642.9",
            "trend": "1642.9",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "1984.6",
            "average": "1639.6",
            "trend": "1644.0",
            "averageUnc": "0.8",
            "trendUnc": "0.7"
        },
        {
            "date": "1984.7",
            "average": "1637.8",
            "trend": "1645.2",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1984.8",
            "average": "1641.3",
            "trend": "1646.4",
            "averageUnc": "1.4",
            "trendUnc": "0.6"
        },
        {
            "date": "1984.9",
            "average": "1650.4",
            "trend": "1647.5",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1984.10",
            "average": "1654.5",
            "trend": "1648.7",
            "averageUnc": "1.4",
            "trendUnc": "0.6"
        },
        {
            "date": "1984.11",
            "average": "1653.7",
            "trend": "1649.8",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1984.12",
            "average": "1656.1",
            "trend": "1651.0",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "1985.1",
            "average": "1655.6",
            "trend": "1652.1",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "1985.2",
            "average": "1652.2",
            "trend": "1653.1",
            "averageUnc": "1.5",
            "trendUnc": "0.6"
        },
        {
            "date": "1985.3",
            "average": "1654.6",
            "trend": "1654.1",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1985.4",
            "average": "1658.2",
            "trend": "1655.2",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1985.5",
            "average": "1655.9",
            "trend": "1656.2",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "1985.6",
            "average": "1650.1",
            "trend": "1657.2",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "1985.7",
            "average": "1646.8",
            "trend": "1658.2",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "1985.8",
            "average": "1652.2",
            "trend": "1659.2",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "1985.9",
            "average": "1662.5",
            "trend": "1660.2",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "1985.10",
            "average": "1667.5",
            "trend": "1661.2",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1985.11",
            "average": "1666.8",
            "trend": "1662.2",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1985.12",
            "average": "1666.1",
            "trend": "1663.3",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1986.1",
            "average": "1666.2",
            "trend": "1664.3",
            "averageUnc": "1.2",
            "trendUnc": "0.7"
        },
        {
            "date": "1986.2",
            "average": "1666.9",
            "trend": "1665.3",
            "averageUnc": "2.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1986.3",
            "average": "1669.3",
            "trend": "1666.4",
            "averageUnc": "1.5",
            "trendUnc": "0.7"
        },
        {
            "date": "1986.4",
            "average": "1670.8",
            "trend": "1667.4",
            "averageUnc": "1.5",
            "trendUnc": "0.8"
        },
        {
            "date": "1986.5",
            "average": "1668.4",
            "trend": "1668.5",
            "averageUnc": "0.9",
            "trendUnc": "0.8"
        },
        {
            "date": "1986.6",
            "average": "1664.8",
            "trend": "1669.6",
            "averageUnc": "1.3",
            "trendUnc": "0.8"
        },
        {
            "date": "1986.7",
            "average": "1662.3",
            "trend": "1670.7",
            "averageUnc": "1.2",
            "trendUnc": "0.8"
        },
        {
            "date": "1986.8",
            "average": "1664.3",
            "trend": "1671.8",
            "averageUnc": "1.6",
            "trendUnc": "0.8"
        },
        {
            "date": "1986.9",
            "average": "1672.6",
            "trend": "1672.9",
            "averageUnc": "1.5",
            "trendUnc": "0.8"
        },
        {
            "date": "1986.10",
            "average": "1678.7",
            "trend": "1674.0",
            "averageUnc": "1.5",
            "trendUnc": "0.8"
        },
        {
            "date": "1986.11",
            "average": "1679.0",
            "trend": "1675.1",
            "averageUnc": "1.7",
            "trendUnc": "0.8"
        },
        {
            "date": "1986.12",
            "average": "1679.1",
            "trend": "1676.2",
            "averageUnc": "1.2",
            "trendUnc": "0.8"
        },
        {
            "date": "1987.1",
            "average": "1679.3",
            "trend": "1677.3",
            "averageUnc": "1.2",
            "trendUnc": "0.8"
        },
        {
            "date": "1987.2",
            "average": "1679.0",
            "trend": "1678.3",
            "averageUnc": "1.1",
            "trendUnc": "0.8"
        },
        {
            "date": "1987.3",
            "average": "1680.1",
            "trend": "1679.3",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "1987.4",
            "average": "1681.4",
            "trend": "1680.4",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1987.5",
            "average": "1681.9",
            "trend": "1681.4",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1987.6",
            "average": "1680.0",
            "trend": "1682.4",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1987.7",
            "average": "1676.0",
            "trend": "1683.3",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1987.8",
            "average": "1677.1",
            "trend": "1684.3",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1987.9",
            "average": "1685.6",
            "trend": "1685.2",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "1987.10",
            "average": "1691.6",
            "trend": "1686.0",
            "averageUnc": "1.1",
            "trendUnc": "0.4"
        },
        {
            "date": "1987.11",
            "average": "1691.1",
            "trend": "1686.9",
            "averageUnc": "0.8",
            "trendUnc": "0.4"
        },
        {
            "date": "1987.12",
            "average": "1690.5",
            "trend": "1687.7",
            "averageUnc": "0.9",
            "trendUnc": "0.4"
        },
        {
            "date": "1988.1",
            "average": "1691.9",
            "trend": "1688.5",
            "averageUnc": "0.7",
            "trendUnc": "0.4"
        },
        {
            "date": "1988.2",
            "average": "1692.5",
            "trend": "1689.3",
            "averageUnc": "0.8",
            "trendUnc": "0.4"
        },
        {
            "date": "1988.3",
            "average": "1691.3",
            "trend": "1690.1",
            "averageUnc": "1.0",
            "trendUnc": "0.4"
        },
        {
            "date": "1988.4",
            "average": "1690.0",
            "trend": "1690.9",
            "averageUnc": "0.9",
            "trendUnc": "0.4"
        },
        {
            "date": "1988.5",
            "average": "1689.0",
            "trend": "1691.8",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1988.6",
            "average": "1687.1",
            "trend": "1692.7",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "1988.7",
            "average": "1685.9",
            "trend": "1693.5",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1988.8",
            "average": "1689.3",
            "trend": "1694.5",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1988.9",
            "average": "1696.3",
            "trend": "1695.4",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1988.10",
            "average": "1701.3",
            "trend": "1696.4",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1988.11",
            "average": "1702.9",
            "trend": "1697.4",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "1988.12",
            "average": "1702.0",
            "trend": "1698.4",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1989.1",
            "average": "1700.6",
            "trend": "1699.4",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1989.2",
            "average": "1701.1",
            "trend": "1700.4",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1989.3",
            "average": "1702.5",
            "trend": "1701.4",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1989.4",
            "average": "1703.7",
            "trend": "1702.4",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1989.5",
            "average": "1703.4",
            "trend": "1703.4",
            "averageUnc": "0.6",
            "trendUnc": "0.6"
        },
        {
            "date": "1989.6",
            "average": "1700.3",
            "trend": "1704.4",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1989.7",
            "average": "1698.2",
            "trend": "1705.3",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1989.8",
            "average": "1702.0",
            "trend": "1706.2",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1989.9",
            "average": "1707.2",
            "trend": "1707.1",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1989.10",
            "average": "1710.5",
            "trend": "1708.0",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "1989.11",
            "average": "1713.1",
            "trend": "1708.8",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1989.12",
            "average": "1713.2",
            "trend": "1709.6",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1990.1",
            "average": "1712.0",
            "trend": "1710.4",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1990.2",
            "average": "1713.3",
            "trend": "1711.1",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1990.3",
            "average": "1714.4",
            "trend": "1711.7",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "1990.4",
            "average": "1712.6",
            "trend": "1712.4",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "1990.5",
            "average": "1710.7",
            "trend": "1713.1",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "1990.6",
            "average": "1708.3",
            "trend": "1713.8",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "1990.7",
            "average": "1706.4",
            "trend": "1714.4",
            "averageUnc": "0.8",
            "trendUnc": "0.7"
        },
        {
            "date": "1990.8",
            "average": "1710.1",
            "trend": "1715.1",
            "averageUnc": "1.2",
            "trendUnc": "0.7"
        },
        {
            "date": "1990.9",
            "average": "1717.6",
            "trend": "1715.8",
            "averageUnc": "1.2",
            "trendUnc": "0.7"
        },
        {
            "date": "1990.10",
            "average": "1722.0",
            "trend": "1716.6",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "1990.11",
            "average": "1723.5",
            "trend": "1717.4",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1990.12",
            "average": "1723.4",
            "trend": "1718.2",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1991.1",
            "average": "1721.6",
            "trend": "1719.2",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1991.2",
            "average": "1721.2",
            "trend": "1720.2",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "1991.3",
            "average": "1722.1",
            "trend": "1721.2",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1991.4",
            "average": "1722.5",
            "trend": "1722.4",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1991.5",
            "average": "1722.2",
            "trend": "1723.6",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1991.6",
            "average": "1719.0",
            "trend": "1724.9",
            "averageUnc": "1.2",
            "trendUnc": "0.7"
        },
        {
            "date": "1991.7",
            "average": "1716.1",
            "trend": "1726.2",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1991.8",
            "average": "1719.2",
            "trend": "1727.5",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "1991.9",
            "average": "1726.2",
            "trend": "1728.8",
            "averageUnc": "1.3",
            "trendUnc": "0.7"
        },
        {
            "date": "1991.10",
            "average": "1732.7",
            "trend": "1730.1",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1991.11",
            "average": "1737.5",
            "trend": "1731.2",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "1991.12",
            "average": "1739.7",
            "trend": "1732.3",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "1992.1",
            "average": "1738.9",
            "trend": "1733.2",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "1992.2",
            "average": "1737.3",
            "trend": "1734.0",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "1992.3",
            "average": "1737.0",
            "trend": "1734.6",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1992.4",
            "average": "1736.6",
            "trend": "1735.1",
            "averageUnc": "0.6",
            "trendUnc": "0.6"
        },
        {
            "date": "1992.5",
            "average": "1734.9",
            "trend": "1735.4",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "1992.6",
            "average": "1731.6",
            "trend": "1735.6",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1992.7",
            "average": "1728.9",
            "trend": "1735.7",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1992.8",
            "average": "1730.4",
            "trend": "1735.7",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1992.9",
            "average": "1734.7",
            "trend": "1735.6",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1992.10",
            "average": "1737.8",
            "trend": "1735.4",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1992.11",
            "average": "1739.3",
            "trend": "1735.3",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "1992.12",
            "average": "1738.6",
            "trend": "1735.2",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1993.1",
            "average": "1735.8",
            "trend": "1735.1",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1993.2",
            "average": "1734.4",
            "trend": "1735.1",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "1993.3",
            "average": "1735.5",
            "trend": "1735.2",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1993.4",
            "average": "1736.7",
            "trend": "1735.3",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1993.5",
            "average": "1735.0",
            "trend": "1735.5",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1993.6",
            "average": "1730.9",
            "trend": "1735.8",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1993.7",
            "average": "1728.0",
            "trend": "1736.2",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1993.8",
            "average": "1731.2",
            "trend": "1736.6",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1993.9",
            "average": "1738.5",
            "trend": "1737.1",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1993.10",
            "average": "1743.3",
            "trend": "1737.6",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1993.11",
            "average": "1745.2",
            "trend": "1738.1",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "1993.12",
            "average": "1744.3",
            "trend": "1738.7",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.1",
            "average": "1741.4",
            "trend": "1739.3",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.2",
            "average": "1740.9",
            "trend": "1739.8",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.3",
            "average": "1741.9",
            "trend": "1740.4",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.4",
            "average": "1741.9",
            "trend": "1741.0",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.5",
            "average": "1740.6",
            "trend": "1741.6",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.6",
            "average": "1736.9",
            "trend": "1742.2",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.7",
            "average": "1732.4",
            "trend": "1742.9",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.8",
            "average": "1734.1",
            "trend": "1743.5",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.9",
            "average": "1743.0",
            "trend": "1744.1",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.10",
            "average": "1749.8",
            "trend": "1744.7",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.11",
            "average": "1751.2",
            "trend": "1745.3",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1994.12",
            "average": "1751.6",
            "trend": "1745.9",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1995.1",
            "average": "1751.0",
            "trend": "1746.5",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1995.2",
            "average": "1749.4",
            "trend": "1747.0",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1995.3",
            "average": "1748.9",
            "trend": "1747.5",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "1995.4",
            "average": "1749.4",
            "trend": "1747.9",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "1995.5",
            "average": "1747.7",
            "trend": "1748.3",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "1995.6",
            "average": "1742.8",
            "trend": "1748.7",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1995.7",
            "average": "1740.1",
            "trend": "1749.0",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1995.8",
            "average": "1743.5",
            "trend": "1749.2",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "1995.9",
            "average": "1749.7",
            "trend": "1749.5",
            "averageUnc": "1.3",
            "trendUnc": "0.5"
        },
        {
            "date": "1995.10",
            "average": "1754.2",
            "trend": "1749.7",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1995.11",
            "average": "1755.3",
            "trend": "1749.9",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1995.12",
            "average": "1753.7",
            "trend": "1750.1",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1996.1",
            "average": "1752.3",
            "trend": "1750.2",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1996.2",
            "average": "1752.9",
            "trend": "1750.4",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "1996.3",
            "average": "1752.4",
            "trend": "1750.6",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1996.4",
            "average": "1749.9",
            "trend": "1750.8",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1996.5",
            "average": "1748.6",
            "trend": "1751.0",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "1996.6",
            "average": "1746.2",
            "trend": "1751.2",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1996.7",
            "average": "1742.2",
            "trend": "1751.4",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "1996.8",
            "average": "1744.7",
            "trend": "1751.7",
            "averageUnc": "1.3",
            "trendUnc": "0.7"
        },
        {
            "date": "1996.9",
            "average": "1753.0",
            "trend": "1751.9",
            "averageUnc": "1.3",
            "trendUnc": "0.7"
        },
        {
            "date": "1996.10",
            "average": "1759.0",
            "trend": "1752.1",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1996.11",
            "average": "1759.9",
            "trend": "1752.3",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1996.12",
            "average": "1756.8",
            "trend": "1752.5",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "1997.1",
            "average": "1753.4",
            "trend": "1752.8",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1997.2",
            "average": "1753.8",
            "trend": "1753.0",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1997.3",
            "average": "1755.6",
            "trend": "1753.2",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1997.4",
            "average": "1755.5",
            "trend": "1753.5",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "1997.5",
            "average": "1753.9",
            "trend": "1753.9",
            "averageUnc": "0.7",
            "trendUnc": "0.4"
        },
        {
            "date": "1997.6",
            "average": "1750.2",
            "trend": "1754.2",
            "averageUnc": "0.9",
            "trendUnc": "0.4"
        },
        {
            "date": "1997.7",
            "average": "1746.2",
            "trend": "1754.7",
            "averageUnc": "1.0",
            "trendUnc": "0.4"
        },
        {
            "date": "1997.8",
            "average": "1747.9",
            "trend": "1755.3",
            "averageUnc": "0.9",
            "trendUnc": "0.4"
        },
        {
            "date": "1997.9",
            "average": "1755.1",
            "trend": "1755.9",
            "averageUnc": "0.9",
            "trendUnc": "0.4"
        },
        {
            "date": "1997.10",
            "average": "1760.2",
            "trend": "1756.6",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1997.11",
            "average": "1761.7",
            "trend": "1757.5",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "1997.12",
            "average": "1761.9",
            "trend": "1758.4",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "1998.1",
            "average": "1761.5",
            "trend": "1759.4",
            "averageUnc": "0.7",
            "trendUnc": "0.5"
        },
        {
            "date": "1998.2",
            "average": "1761.5",
            "trend": "1760.5",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "1998.3",
            "average": "1763.0",
            "trend": "1761.6",
            "averageUnc": "1.6",
            "trendUnc": "0.6"
        },
        {
            "date": "1998.4",
            "average": "1764.7",
            "trend": "1762.8",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "1998.5",
            "average": "1764.2",
            "trend": "1764.0",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1998.6",
            "average": "1760.3",
            "trend": "1765.1",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "1998.7",
            "average": "1756.1",
            "trend": "1766.3",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1998.8",
            "average": "1760.1",
            "trend": "1767.4",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1998.9",
            "average": "1770.5",
            "trend": "1768.4",
            "averageUnc": "1.3",
            "trendUnc": "0.7"
        },
        {
            "date": "1998.10",
            "average": "1776.2",
            "trend": "1769.3",
            "averageUnc": "1.3",
            "trendUnc": "0.7"
        },
        {
            "date": "1998.11",
            "average": "1775.6",
            "trend": "1770.1",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "1998.12",
            "average": "1774.2",
            "trend": "1770.7",
            "averageUnc": "0.8",
            "trendUnc": "0.7"
        },
        {
            "date": "1999.1",
            "average": "1774.0",
            "trend": "1771.3",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "1999.2",
            "average": "1774.2",
            "trend": "1771.8",
            "averageUnc": "1.5",
            "trendUnc": "0.7"
        },
        {
            "date": "1999.3",
            "average": "1774.7",
            "trend": "1772.2",
            "averageUnc": "1.2",
            "trendUnc": "0.7"
        },
        {
            "date": "1999.4",
            "average": "1774.9",
            "trend": "1772.5",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "1999.5",
            "average": "1772.7",
            "trend": "1772.8",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "1999.6",
            "average": "1767.4",
            "trend": "1773.0",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "1999.7",
            "average": "1763.0",
            "trend": "1773.1",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "1999.8",
            "average": "1764.7",
            "trend": "1773.2",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "1999.9",
            "average": "1771.1",
            "trend": "1773.3",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "1999.10",
            "average": "1776.6",
            "trend": "1773.4",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "1999.11",
            "average": "1778.6",
            "trend": "1773.4",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "1999.12",
            "average": "1777.3",
            "trend": "1773.4",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2000.1",
            "average": "1775.7",
            "trend": "1773.5",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2000.2",
            "average": "1775.8",
            "trend": "1773.5",
            "averageUnc": "1.4",
            "trendUnc": "0.7"
        },
        {
            "date": "2000.3",
            "average": "1776.9",
            "trend": "1773.4",
            "averageUnc": "1.5",
            "trendUnc": "0.7"
        },
        {
            "date": "2000.4",
            "average": "1777.4",
            "trend": "1773.4",
            "averageUnc": "1.4",
            "trendUnc": "0.7"
        },
        {
            "date": "2000.5",
            "average": "1774.6",
            "trend": "1773.3",
            "averageUnc": "1.2",
            "trendUnc": "0.8"
        },
        {
            "date": "2000.6",
            "average": "1768.2",
            "trend": "1773.2",
            "averageUnc": "1.1",
            "trendUnc": "0.8"
        },
        {
            "date": "2000.7",
            "average": "1763.6",
            "trend": "1773.1",
            "averageUnc": "0.8",
            "trendUnc": "0.8"
        },
        {
            "date": "2000.8",
            "average": "1765.7",
            "trend": "1772.9",
            "averageUnc": "1.0",
            "trendUnc": "0.8"
        },
        {
            "date": "2000.9",
            "average": "1772.2",
            "trend": "1772.7",
            "averageUnc": "1.1",
            "trendUnc": "0.8"
        },
        {
            "date": "2000.10",
            "average": "1777.1",
            "trend": "1772.5",
            "averageUnc": "0.8",
            "trendUnc": "0.7"
        },
        {
            "date": "2000.11",
            "average": "1777.7",
            "trend": "1772.3",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2000.12",
            "average": "1775.3",
            "trend": "1772.1",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2001.1",
            "average": "1772.9",
            "trend": "1771.9",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "2001.2",
            "average": "1772.5",
            "trend": "1771.7",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2001.3",
            "average": "1773.7",
            "trend": "1771.5",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2001.4",
            "average": "1773.9",
            "trend": "1771.3",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "2001.5",
            "average": "1770.8",
            "trend": "1771.2",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2001.6",
            "average": "1765.9",
            "trend": "1771.1",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2001.7",
            "average": "1762.8",
            "trend": "1771.1",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2001.8",
            "average": "1764.3",
            "trend": "1771.0",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2001.9",
            "average": "1770.5",
            "trend": "1771.0",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "2001.10",
            "average": "1775.5",
            "trend": "1771.1",
            "averageUnc": "0.6",
            "trendUnc": "0.5"
        },
        {
            "date": "2001.11",
            "average": "1776.6",
            "trend": "1771.1",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "2001.12",
            "average": "1775.9",
            "trend": "1771.2",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2002.1",
            "average": "1774.1",
            "trend": "1771.3",
            "averageUnc": "1.2",
            "trendUnc": "0.4"
        },
        {
            "date": "2002.2",
            "average": "1772.8",
            "trend": "1771.4",
            "averageUnc": "1.0",
            "trendUnc": "0.4"
        },
        {
            "date": "2002.3",
            "average": "1773.4",
            "trend": "1771.6",
            "averageUnc": "0.6",
            "trendUnc": "0.4"
        },
        {
            "date": "2002.4",
            "average": "1772.7",
            "trend": "1771.7",
            "averageUnc": "0.6",
            "trendUnc": "0.4"
        },
        {
            "date": "2002.5",
            "average": "1770.3",
            "trend": "1771.9",
            "averageUnc": "0.7",
            "trendUnc": "0.5"
        },
        {
            "date": "2002.6",
            "average": "1766.9",
            "trend": "1772.1",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "2002.7",
            "average": "1764.3",
            "trend": "1772.4",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2002.8",
            "average": "1767.0",
            "trend": "1772.7",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2002.9",
            "average": "1773.8",
            "trend": "1773.0",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2002.10",
            "average": "1778.2",
            "trend": "1773.4",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2002.11",
            "average": "1779.6",
            "trend": "1773.8",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2002.12",
            "average": "1779.7",
            "trend": "1774.2",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2003.1",
            "average": "1777.5",
            "trend": "1774.8",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2003.2",
            "average": "1774.8",
            "trend": "1775.3",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2003.3",
            "average": "1774.8",
            "trend": "1775.8",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2003.4",
            "average": "1775.7",
            "trend": "1776.4",
            "averageUnc": "1.3",
            "trendUnc": "0.5"
        },
        {
            "date": "2003.5",
            "average": "1774.4",
            "trend": "1777.0",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2003.6",
            "average": "1771.7",
            "trend": "1777.5",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "2003.7",
            "average": "1770.7",
            "trend": "1778.0",
            "averageUnc": "1.8",
            "trendUnc": "0.5"
        },
        {
            "date": "2003.8",
            "average": "1774.2",
            "trend": "1778.5",
            "averageUnc": "1.6",
            "trendUnc": "0.5"
        },
        {
            "date": "2003.9",
            "average": "1780.5",
            "trend": "1778.8",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2003.10",
            "average": "1784.7",
            "trend": "1779.1",
            "averageUnc": "0.7",
            "trendUnc": "0.5"
        },
        {
            "date": "2003.11",
            "average": "1785.3",
            "trend": "1779.3",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2003.12",
            "average": "1783.6",
            "trend": "1779.3",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2004.1",
            "average": "1780.9",
            "trend": "1779.2",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2004.2",
            "average": "1779.9",
            "trend": "1779.1",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2004.3",
            "average": "1781.0",
            "trend": "1778.8",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2004.4",
            "average": "1780.7",
            "trend": "1778.4",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2004.5",
            "average": "1777.6",
            "trend": "1777.9",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2004.6",
            "average": "1772.3",
            "trend": "1777.4",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2004.7",
            "average": "1768.0",
            "trend": "1776.9",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2004.8",
            "average": "1769.7",
            "trend": "1776.3",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2004.9",
            "average": "1775.5",
            "trend": "1775.8",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2004.10",
            "average": "1779.7",
            "trend": "1775.3",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2004.11",
            "average": "1780.5",
            "trend": "1774.9",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2004.12",
            "average": "1778.3",
            "trend": "1774.6",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.1",
            "average": "1776.0",
            "trend": "1774.3",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.2",
            "average": "1775.6",
            "trend": "1774.1",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.3",
            "average": "1775.5",
            "trend": "1774.1",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.4",
            "average": "1774.6",
            "trend": "1774.0",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.5",
            "average": "1772.3",
            "trend": "1774.1",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.6",
            "average": "1768.7",
            "trend": "1774.2",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.7",
            "average": "1766.3",
            "trend": "1774.3",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.8",
            "average": "1768.0",
            "trend": "1774.4",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.9",
            "average": "1773.2",
            "trend": "1774.5",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.10",
            "average": "1778.6",
            "trend": "1774.6",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.11",
            "average": "1781.1",
            "trend": "1774.7",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2005.12",
            "average": "1780.1",
            "trend": "1774.8",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2006.1",
            "average": "1779.4",
            "trend": "1774.8",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2006.2",
            "average": "1779.4",
            "trend": "1774.8",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2006.3",
            "average": "1777.4",
            "trend": "1774.7",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "2006.4",
            "average": "1776.1",
            "trend": "1774.7",
            "averageUnc": "0.7",
            "trendUnc": "0.5"
        },
        {
            "date": "2006.5",
            "average": "1775.0",
            "trend": "1774.7",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2006.6",
            "average": "1769.3",
            "trend": "1774.7",
            "averageUnc": "1.3",
            "trendUnc": "0.5"
        },
        {
            "date": "2006.7",
            "average": "1764.2",
            "trend": "1774.8",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "2006.8",
            "average": "1767.2",
            "trend": "1774.9",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "2006.9",
            "average": "1774.6",
            "trend": "1775.2",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2006.10",
            "average": "1778.2",
            "trend": "1775.5",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2006.11",
            "average": "1779.0",
            "trend": "1775.9",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "2006.12",
            "average": "1779.9",
            "trend": "1776.4",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.1",
            "average": "1779.2",
            "trend": "1777.0",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.2",
            "average": "1778.7",
            "trend": "1777.6",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.3",
            "average": "1780.3",
            "trend": "1778.3",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.4",
            "average": "1781.1",
            "trend": "1779.0",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.5",
            "average": "1779.4",
            "trend": "1779.8",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.6",
            "average": "1775.6",
            "trend": "1780.5",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.7",
            "average": "1772.6",
            "trend": "1781.2",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.8",
            "average": "1777.2",
            "trend": "1781.9",
            "averageUnc": "1.5",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.9",
            "average": "1785.9",
            "trend": "1782.6",
            "averageUnc": "1.5",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.10",
            "average": "1789.9",
            "trend": "1783.2",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2007.11",
            "average": "1789.5",
            "trend": "1783.7",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2007.12",
            "average": "1788.2",
            "trend": "1784.3",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.1",
            "average": "1786.8",
            "trend": "1784.8",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.2",
            "average": "1785.8",
            "trend": "1785.3",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.3",
            "average": "1786.1",
            "trend": "1785.8",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.4",
            "average": "1786.8",
            "trend": "1786.3",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.5",
            "average": "1785.1",
            "trend": "1786.8",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.6",
            "average": "1780.4",
            "trend": "1787.3",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.7",
            "average": "1777.6",
            "trend": "1787.9",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.8",
            "average": "1781.0",
            "trend": "1788.5",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.9",
            "average": "1787.7",
            "trend": "1789.0",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.10",
            "average": "1793.7",
            "trend": "1789.6",
            "averageUnc": "0.7",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.11",
            "average": "1797.4",
            "trend": "1790.2",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2008.12",
            "average": "1796.7",
            "trend": "1790.8",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2009.1",
            "average": "1795.1",
            "trend": "1791.4",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2009.2",
            "average": "1795.6",
            "trend": "1791.9",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "2009.3",
            "average": "1796.1",
            "trend": "1792.3",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2009.4",
            "average": "1795.6",
            "trend": "1792.8",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2009.5",
            "average": "1792.3",
            "trend": "1793.2",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "2009.6",
            "average": "1786.9",
            "trend": "1793.6",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2009.7",
            "average": "1784.9",
            "trend": "1794.0",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "2009.8",
            "average": "1788.8",
            "trend": "1794.3",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2009.9",
            "average": "1794.8",
            "trend": "1794.6",
            "averageUnc": "1.2",
            "trendUnc": "0.7"
        },
        {
            "date": "2009.10",
            "average": "1798.0",
            "trend": "1794.9",
            "averageUnc": "1.4",
            "trendUnc": "0.7"
        },
        {
            "date": "2009.11",
            "average": "1797.9",
            "trend": "1795.2",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2009.12",
            "average": "1796.7",
            "trend": "1795.6",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.1",
            "average": "1797.1",
            "trend": "1795.9",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.2",
            "average": "1798.7",
            "trend": "1796.3",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.3",
            "average": "1799.4",
            "trend": "1796.7",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.4",
            "average": "1799.6",
            "trend": "1797.1",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.5",
            "average": "1797.7",
            "trend": "1797.5",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.6",
            "average": "1792.6",
            "trend": "1797.9",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.7",
            "average": "1789.4",
            "trend": "1798.4",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.8",
            "average": "1794.0",
            "trend": "1798.9",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.9",
            "average": "1801.8",
            "trend": "1799.3",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.10",
            "average": "1806.5",
            "trend": "1799.8",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2010.11",
            "average": "1807.0",
            "trend": "1800.3",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2010.12",
            "average": "1803.6",
            "trend": "1800.7",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.1",
            "average": "1800.5",
            "trend": "1801.2",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.2",
            "average": "1800.2",
            "trend": "1801.6",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.3",
            "average": "1801.0",
            "trend": "1802.0",
            "averageUnc": "0.7",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.4",
            "average": "1802.9",
            "trend": "1802.4",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.5",
            "average": "1803.3",
            "trend": "1802.8",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.6",
            "average": "1799.2",
            "trend": "1803.2",
            "averageUnc": "0.7",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.7",
            "average": "1796.1",
            "trend": "1803.6",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.8",
            "average": "1798.9",
            "trend": "1804.0",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.9",
            "average": "1804.0",
            "trend": "1804.4",
            "averageUnc": "1.6",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.10",
            "average": "1809.5",
            "trend": "1804.8",
            "averageUnc": "1.6",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.11",
            "average": "1812.3",
            "trend": "1805.2",
            "averageUnc": "1.3",
            "trendUnc": "0.7"
        },
        {
            "date": "2011.12",
            "average": "1810.0",
            "trend": "1805.6",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2012.1",
            "average": "1807.3",
            "trend": "1806.0",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2012.2",
            "average": "1808.3",
            "trend": "1806.4",
            "averageUnc": "1.4",
            "trendUnc": "0.7"
        },
        {
            "date": "2012.3",
            "average": "1810.0",
            "trend": "1806.9",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2012.4",
            "average": "1808.4",
            "trend": "1807.3",
            "averageUnc": "0.6",
            "trendUnc": "0.7"
        },
        {
            "date": "2012.5",
            "average": "1804.7",
            "trend": "1807.8",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2012.6",
            "average": "1800.9",
            "trend": "1808.2",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2012.7",
            "average": "1799.2",
            "trend": "1808.6",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2012.8",
            "average": "1803.2",
            "trend": "1809.1",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2012.9",
            "average": "1810.1",
            "trend": "1809.5",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2012.10",
            "average": "1814.7",
            "trend": "1809.9",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2012.11",
            "average": "1815.9",
            "trend": "1810.3",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2012.12",
            "average": "1814.6",
            "trend": "1810.6",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.1",
            "average": "1814.1",
            "trend": "1811.0",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.2",
            "average": "1814.2",
            "trend": "1811.3",
            "averageUnc": "1.6",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.3",
            "average": "1813.3",
            "trend": "1811.6",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.4",
            "average": "1812.8",
            "trend": "1812.0",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.5",
            "average": "1811.9",
            "trend": "1812.3",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.6",
            "average": "1808.5",
            "trend": "1812.7",
            "averageUnc": "1.4",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.7",
            "average": "1805.7",
            "trend": "1813.1",
            "averageUnc": "1.5",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.8",
            "average": "1808.4",
            "trend": "1813.6",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.9",
            "average": "1814.3",
            "trend": "1814.1",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.10",
            "average": "1818.6",
            "trend": "1814.7",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.11",
            "average": "1820.4",
            "trend": "1815.4",
            "averageUnc": "0.7",
            "trendUnc": "0.6"
        },
        {
            "date": "2013.12",
            "average": "1819.4",
            "trend": "1816.1",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2014.1",
            "average": "1816.9",
            "trend": "1817.0",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2014.2",
            "average": "1816.4",
            "trend": "1817.9",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2014.3",
            "average": "1818.1",
            "trend": "1818.8",
            "averageUnc": "1.2",
            "trendUnc": "0.5"
        },
        {
            "date": "2014.4",
            "average": "1820.9",
            "trend": "1819.9",
            "averageUnc": "0.6",
            "trendUnc": "0.5"
        },
        {
            "date": "2014.5",
            "average": "1821.9",
            "trend": "1820.9",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "2014.6",
            "average": "1818.4",
            "trend": "1822.1",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "2014.7",
            "average": "1815.6",
            "trend": "1823.2",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2014.8",
            "average": "1819.8",
            "trend": "1824.4",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2014.9",
            "average": "1827.0",
            "trend": "1825.5",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2014.10",
            "average": "1831.3",
            "trend": "1826.6",
            "averageUnc": "0.6",
            "trendUnc": "0.5"
        },
        {
            "date": "2014.11",
            "average": "1833.1",
            "trend": "1827.7",
            "averageUnc": "0.6",
            "trendUnc": "0.5"
        },
        {
            "date": "2014.12",
            "average": "1833.5",
            "trend": "1828.8",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "2015.1",
            "average": "1832.9",
            "trend": "1829.8",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2015.2",
            "average": "1832.7",
            "trend": "1830.7",
            "averageUnc": "0.8",
            "trendUnc": "0.5"
        },
        {
            "date": "2015.3",
            "average": "1833.1",
            "trend": "1831.6",
            "averageUnc": "0.7",
            "trendUnc": "0.5"
        },
        {
            "date": "2015.4",
            "average": "1833.2",
            "trend": "1832.5",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2015.5",
            "average": "1831.8",
            "trend": "1833.4",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2015.6",
            "average": "1827.4",
            "trend": "1834.2",
            "averageUnc": "0.9",
            "trendUnc": "0.5"
        },
        {
            "date": "2015.7",
            "average": "1824.8",
            "trend": "1835.0",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2015.8",
            "average": "1829.2",
            "trend": "1835.8",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2015.9",
            "average": "1836.2",
            "trend": "1836.6",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2015.10",
            "average": "1841.5",
            "trend": "1837.4",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2015.11",
            "average": "1844.7",
            "trend": "1838.2",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2015.12",
            "average": "1844.9",
            "trend": "1838.9",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2016.1",
            "average": "1842.4",
            "trend": "1839.7",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2016.2",
            "average": "1841.6",
            "trend": "1840.4",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2016.3",
            "average": "1843.0",
            "trend": "1841.0",
            "averageUnc": "0.8",
            "trendUnc": "0.7"
        },
        {
            "date": "2016.4",
            "average": "1843.7",
            "trend": "1841.7",
            "averageUnc": "0.7",
            "trendUnc": "0.7"
        },
        {
            "date": "2016.5",
            "average": "1842.1",
            "trend": "1842.3",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2016.6",
            "average": "1837.9",
            "trend": "1843.0",
            "averageUnc": "1.2",
            "trendUnc": "0.7"
        },
        {
            "date": "2016.7",
            "average": "1834.2",
            "trend": "1843.5",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2016.8",
            "average": "1836.7",
            "trend": "1844.1",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2016.9",
            "average": "1844.2",
            "trend": "1844.6",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2016.10",
            "average": "1849.9",
            "trend": "1845.1",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2016.11",
            "average": "1851.4",
            "trend": "1845.6",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2016.12",
            "average": "1851.1",
            "trend": "1846.1",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2017.1",
            "average": "1849.8",
            "trend": "1846.6",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2017.2",
            "average": "1848.5",
            "trend": "1847.1",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2017.3",
            "average": "1848.3",
            "trend": "1847.6",
            "averageUnc": "1.4",
            "trendUnc": "0.6"
        },
        {
            "date": "2017.4",
            "average": "1848.6",
            "trend": "1848.1",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2017.5",
            "average": "1847.2",
            "trend": "1848.6",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2017.6",
            "average": "1843.0",
            "trend": "1849.2",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2017.7",
            "average": "1840.4",
            "trend": "1849.7",
            "averageUnc": "1.3",
            "trendUnc": "0.7"
        },
        {
            "date": "2017.8",
            "average": "1844.6",
            "trend": "1850.3",
            "averageUnc": "1.2",
            "trendUnc": "0.7"
        },
        {
            "date": "2017.9",
            "average": "1852.8",
            "trend": "1850.9",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "2017.10",
            "average": "1858.1",
            "trend": "1851.6",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2017.11",
            "average": "1858.7",
            "trend": "1852.2",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "2017.12",
            "average": "1856.7",
            "trend": "1852.9",
            "averageUnc": "1.0",
            "trendUnc": "0.7"
        },
        {
            "date": "2018.1",
            "average": "1854.5",
            "trend": "1853.6",
            "averageUnc": "1.0",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.2",
            "average": "1855.0",
            "trend": "1854.3",
            "averageUnc": "0.9",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.3",
            "average": "1856.9",
            "trend": "1855.0",
            "averageUnc": "0.9",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.4",
            "average": "1856.7",
            "trend": "1855.7",
            "averageUnc": "1.1",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.5",
            "average": "1854.8",
            "trend": "1856.4",
            "averageUnc": "1.6",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.6",
            "average": "1852.0",
            "trend": "1857.2",
            "averageUnc": "1.5",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.7",
            "average": "1849.0",
            "trend": "1857.9",
            "averageUnc": "1.5",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.8",
            "average": "1851.9",
            "trend": "1858.7",
            "averageUnc": "1.6",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.9",
            "average": "1860.5",
            "trend": "1859.4",
            "averageUnc": "0.9",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.10",
            "average": "1865.7",
            "trend": "1860.1",
            "averageUnc": "1.1",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.11",
            "average": "1866.2",
            "trend": "1860.9",
            "averageUnc": "1.2",
            "trendUnc": "0.8"
        },
        {
            "date": "2018.12",
            "average": "1866.0",
            "trend": "1861.6",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2019.1",
            "average": "1865.0",
            "trend": "1862.3",
            "averageUnc": "1.1",
            "trendUnc": "0.7"
        },
        {
            "date": "2019.2",
            "average": "1865.0",
            "trend": "1863.0",
            "averageUnc": "0.8",
            "trendUnc": "0.7"
        },
        {
            "date": "2019.3",
            "average": "1866.3",
            "trend": "1863.7",
            "averageUnc": "0.9",
            "trendUnc": "0.7"
        },
        {
            "date": "2019.4",
            "average": "1865.3",
            "trend": "1864.4",
            "averageUnc": "0.6",
            "trendUnc": "0.6"
        },
        {
            "date": "2019.5",
            "average": "1861.9",
            "trend": "1865.1",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2019.6",
            "average": "1858.8",
            "trend": "1865.9",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2019.7",
            "average": "1858.4",
            "trend": "1866.7",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2019.8",
            "average": "1863.0",
            "trend": "1867.5",
            "averageUnc": "1.3",
            "trendUnc": "0.5"
        },
        {
            "date": "2019.9",
            "average": "1870.8",
            "trend": "1868.3",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2019.10",
            "average": "1875.4",
            "trend": "1869.2",
            "averageUnc": "1.1",
            "trendUnc": "0.5"
        },
        {
            "date": "2019.11",
            "average": "1875.5",
            "trend": "1870.2",
            "averageUnc": "1.0",
            "trendUnc": "0.5"
        },
        {
            "date": "2019.12",
            "average": "1874.7",
            "trend": "1871.2",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.1",
            "average": "1873.2",
            "trend": "1872.2",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.2",
            "average": "1872.7",
            "trend": "1873.3",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.3",
            "average": "1874.8",
            "trend": "1874.4",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.4",
            "average": "1875.9",
            "trend": "1875.5",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.5",
            "average": "1874.3",
            "trend": "1876.7",
            "averageUnc": "1.1",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.6",
            "average": "1871.9",
            "trend": "1878.0",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.7",
            "average": "1871.5",
            "trend": "1879.2",
            "averageUnc": "1.3",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.8",
            "average": "1876.5",
            "trend": "1880.5",
            "averageUnc": "1.2",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.9",
            "average": "1884.7",
            "trend": "1881.9",
            "averageUnc": "1.0",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.10",
            "average": "1890.1",
            "trend": "1883.2",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.11",
            "average": "1891.8",
            "trend": "1884.6",
            "averageUnc": "0.6",
            "trendUnc": "0.6"
        },
        {
            "date": "2020.12",
            "average": "1892.2",
            "trend": "1886.1",
            "averageUnc": "0.8",
            "trendUnc": "0.6"
        },
        {
            "date": "2021.1",
            "average": "1890.4",
            "trend": "1887.6",
            "averageUnc": "0.9",
            "trendUnc": "0.6"
        },
        {
            "date": "2021.2",
            "average": "1888.0",
            "trend": "1889.1",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.3",
            "average": "1888.8",
            "trend": "1890.6",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.4",
            "average": "1891.2",
            "trend": "1892.1",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.5",
            "average": "1891.6",
            "trend": "1893.8",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.6",
            "average": "1888.6",
            "trend": "1895.4",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.7",
            "average": "1886.5",
            "trend": "1897.0",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.8",
            "average": "1892.7",
            "trend": "1898.6",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.9",
            "average": "1902.7",
            "trend": "1900.2",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.10",
            "average": "1908.0",
            "trend": "1901.7",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.11",
            "average": "1909.5",
            "trend": "1903.2",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2021.12",
            "average": "1909.6",
            "trend": "1904.5",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2022.1",
            "average": "1908.7",
            "trend": "1905.8",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2022.2",
            "average": "1908.5",
            "trend": "1906.9",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        },
        {
            "date": "2022.3",
            "average": "1909.2",
            "trend": "1907.8",
            "averageUnc": "-9.9",
            "trendUnc": "-9.9"
        }
    ]
}
    return data



#does the UPDATING
@app.route('/thought/<int:id>/update', methods = ['POST'])
def thought_update(id):
    #VALIDATIONS
    if not model_thought.Thought.validator(request.form):
        return redirect(f'/thought/{id}/edit')
#if it passes validation, call it
    data = {
        **request.form,
        'id':id
    }
    model_thought.Thought.update_one(data)
    return redirect('/')


#deleting name
@app.route('/thought/<int:id>/delete')
def thought_delete(id):
    data = {
        'id' : id
    }
    model_thought.Thought.delete_one(data)
    return redirect('/')
