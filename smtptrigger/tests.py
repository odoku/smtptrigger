#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest
import os
import ConfigParser
import StringIO
import smtptrigger as sf
import socket

rootpath = os.path.dirname(os.path.abspath(__file__))

class TestSMTPTrigger(unittest.TestCase):
    config_string = """[server]
host = localhost
port = 20025

[log]
path = smtptrigger.log

[trigger:test001]
pattern = \w+@test001.com
command = touch %(test001)s

[trigger:test002]
pattern = \w+@test002.com
command = touch %(test002)s
""" % {
    'test001': os.path.join(rootpath, 'test001'),
    'test002': os.path.join(rootpath, 'test002'),
}

    mail = """From: =?iso-2022-jp?B?GyRCPi5MbkBuGyhCIBskQjYpGyhC?= <honebone@i.softbank.jp>
Content-Type: multipart/mixed;
    boundary="Apple-Mail=_682EF258-D8A0-4E0D-A757-A30ADB69D218"
X-Smtp-Server: localhost
Subject: =?iso-2022-jp?B?GyRCJFskMiRbJDIbKEI=?=
Message-Id: <4281C0E0-4215-4223-B27B-D92CD9096E55@i.softbank.jp>
X-Universally-Unique-Identifier: 2118ac94-0fbf-486c-a047-5e4d8a4937aa
Date: Sat, 23 Mar 2013 20:07:59 +0900
To: "hoge@shimocolle.odoku.net" <hoge@shimocolle.odoku.net>
Mime-Version: 1.0 (Mac OS X Mail 6.2 \(1499\))


--Apple-Mail=_682EF258-D8A0-4E0D-A757-A30ADB69D218
Content-Transfer-Encoding: 7bit
Content-Type: text/plain;
    charset=iso-2022-jp

わーわーわー


--Apple-Mail=_682EF258-D8A0-4E0D-A757-A30ADB69D218
Content-Disposition: attachment;
    filename*=iso-2022-jp''%1B%24B7W%3B%3B%3C0%1B%28B.html
Content-Type: text/html;
    x-unix-mode=0644;
    name="=?iso-2022-jp?B?GyRCN1c7OzwwGyhCLmh0bWw=?="
Content-Transfer-Encoding: quoted-printable

<!DOCTYPE html>
<html>
<head>
<meta http-equiv=3D"Content-Type" content=3D"text/html; charset=3Dutf-8" =
/>
<meta name=3D"generated-by" content=3D"Markdown PRO, =
http://markdownpro.com"/>
<title></title>
<style type=3D"text/css">

</style><style type=3D"text/css">
/* line 5, scss/simply.scss */
body {
  font-family: "Helvetica Neue", Helvetica, Arial, Geneva, sans-serif;
  font-size: 13px;
  margin: 10px 10px 10px 30px;
  color: #26240c;
}

/* line 13, scss/simply.scss */
h1 {
  margin: 50px 0px 60px -20px;
  letter-spacing: -2px;
  font-weight: bold;
  color: #594c25;
}

/* line 20, scss/simply.scss */
h2 {
  background-color: #e3e8d1;
  color: #594c25;
  margin: 60px 0px 20px -20px;
  padding: 0px 10px;
  font-size: 20px;
  letter-spacing: 2px;
  font-weight: bold;
  -webkit-border-radius: 3px;
  -moz-border-radius: 3px;
  border-radius: 3px;
  -moz-border-radius: 3px;
  border-radius: 3px;
}

/* line 37, scss/simply.scss */
h3, h4, h5, h6 {
  border-bottom: 1px solid #e3e8d1;
  margin: 20px 0px 20px 0px;
}

/* line 42, scss/simply.scss */
p {
  font-family: "Helvetica Neue", Helvetica, Arial, Geneva, sans-serif;
  line-height: 1.8em;
  margin: 20px 0px;
}

/* line 49, scss/simply.scss */
ul li {
  padding: 3px 0px;
  color: #26240c;
}

/* line 55, scss/simply.scss */
a {
  color: #0A8A6D;
  text-decoration: underline;
}
/* line 59, scss/simply.scss */
a:visited {
  color: #0A8A6D;
  text-decoration: underline;
}
/* line 64, scss/simply.scss */
a a:hover {
  color: #00665D;
}

/* line 69, scss/simply.scss */
blockquote {
  padding: 5px 10px;
  border-left: 7px solid #ffccaa;
  padding: 10px 0px 10px 10px;
  margin: 15px 0px;
  color: #333;
  letter-spacing: px;
  font-style: italic;
  font-variant: normal;
}
/* line 79, scss/simply.scss */
blockquote > p {
  margin: 20px 0px;
}

/* line 84, scss/simply.scss */
pre {
  background-color: #f1f1f1;
  padding: 10px;
}
/* line 88, scss/simply.scss */
pre > code {
  margin: 0;
  padding: 0;
  border: 0;
}

</style></head>
<body>
<h1>=E3=83=AC=E3=82=A4=E3=83=89=E3=83=9C=E3=82=B9=E3=83=90=E3=83=88=E3=83=AB=
=E3=81=AE=E3=83=AB=E3=83=BC=E3=83=AB</h1>

<h2>=E5=87=BA=E7=8F=BE=E3=81=99=E3=82=8B=E5=86=85=E5=AE=B9</h2>

<h3>=E9=80=9A=E5=B8=B8=E6=99=82</h3>

<ul>
<li>  =E6=94=BB=E6=92=83=EF=BC=88=E3=83=80=E3=83=A1=E3=83=BC=E3=82=B8=EF=BC=
=89

<ul>
<li>  =E6=8A=BC=E3=81=97=E9=A0=86=E3=81=82=E3=82=8A

<ul>
<li>  =E3=82=A2=E3=82=BF=E3=83=AA</li>
<li>  =E3=83=8F=E3=82=BA=E3=83=AC</li>
</ul></li>
<li>  =E6=8A=BC=E3=81=97=E9=A0=86=E3=81=AA=E3=81=97

<ul>
<li>  =E3=82=A2=E3=82=BF=E3=83=AA</li>
<li>  =E3=83=8F=E3=82=BA=E3=83=AC</li>
</ul></li>
</ul></li>
<li>  =E9=98=B2=E5=BE=A1=EF=BC=88=E3=82=B2=E3=83=BC=E3=83=A0=E6=95=B0=E4=B8=
=8A=E4=B9=97=E3=81=9B=EF=BC=89

<ul>
<li>  =E6=8A=BC=E3=81=97=E9=A0=86=E3=81=82=E3=82=8A

<ul>
<li>  =E3=82=A2=E3=82=BF=E3=83=AA</li>
<li>  =E3=83=8F=E3=82=BA=E3=83=AC</li>
</ul></li>
<li>  =E6=8A=BC=E3=81=97=E9=A0=86=E3=81=AA=E3=81=97

<ul>
<li>  =E3=82=A2=E3=82=BF=E3=83=AA</li>
<li>  =E3=83=8F=E3=82=BA=E3=83=AC</li>
</ul></li>
</ul></li>
<li>  =E3=83=A9=E3=83=83=E3=82=B7=E3=83=A5=EF=BC=88=E3=83=80=E3=83=A1=E3=83=
=BC=E3=82=B8=EF=BC=89</li>
</ul>

<h3>=E3=82=B2=E3=83=BC=E3=83=A0=E7=B5=82=E4=BA=86=EF=BC=88=E7=B6=99=E7=B6=9A=
=E5=88=A4=E5=AE=9A=EF=BC=89=E6=99=82</h3>

<ul>
<li>  =E5=8B=9D=E5=88=A9</li>
<li>  =E6=95=97=E5=8C=97</li>
<li>  =E5=BE=A9=E6=B4=BB</li>
</ul>

<h2>=E9=80=9A=E5=B8=B8=E6=99=82=E3=80=81=E5=90=84=E9=A0=85=E7=9B=AE=E3=81=AE=
=E5=87=BA=E7=8F=BE=E7=A2=BA=E7=8E=87</h2>

=
<p><strong>=E3=80=90=E3=83=AC=E3=82=A4=E3=83=89=E3=83=9C=E3=82=B9=EF=BC=9A=
=E3=83=86=E3=83=B3=E3=83=97=E3=83=AC=E3=83=BC=E3=83=88=E3=80=91=E3=81=A7=E8=
=A8=AD=E5=AE=9A=E5=8F=AF=E8=83=BD</strong></p>

<ul>
<li>  =E6=94=BB=E6=92=83=EF=BC=9A80%</li>
<li>  =E9=98=B2=E5=BE=A1=EF=BC=9A10%</li>
<li>  =E3=83=A9=E3=83=83=E3=82=B7=E3=83=A5=EF=BC=9A10%</li>
</ul>

=
<p>=E6=94=BB=E6=92=83=E3=83=BB=E9=98=B2=E5=BE=A1=E6=99=82=E3=81=AE=E6=8A=BC=
=E3=81=97=E9=A0=86=E3=81=AE=E6=9C=89=E7=84=A1=E3=81=AF=E4=B8=80=E5=BE=8B50=
%=E3=81=AE=E7=A2=BA=E7=8E=87=E3=81=A7=E6=B1=BA=E5=AE=9A=E3=80=82</p>

<h2>=E3=82=B2=E3=83=BC=E3=83=A0=E7=B5=82=E4=BA=86=E6=99=82=E3=81=AE=E7=B6=99=
=E7=B6=9A=E7=A2=BA=E7=8E=87</h2>

=
<p>=E5=8B=9D=E5=88=A9=EF=BC=88=E7=B6=99=E7=B6=9A=EF=BC=89=E3=81=99=E3=82=8B=
=E7=A2=BA=E7=8E=87=E3=81=AF=E4=BB=A5=E4=B8=8B=E3=81=AE=E6=96=B9=E6=B3=95=E3=
=81=A7=E5=9F=BA=E6=9C=AC=E5=80=A4=E3=82=92=E7=AE=97=E5=87=BA</p>

<pre><code>=E5=9F=BA=E6=9C=AC=E5=80=A4 =3D (=E3=83=97=E3=83=AC=E3=82=A4=E3=
=83=A4=E3=83=BC=E3=81=AE=E6=88=A6=E9=97=98=E5=8A=9B - =
=E3=83=9C=E3=82=B9=E3=81=AE=E6=88=A6=E9=97=98=E5=8A=9B) * 0.005 + 50
</code></pre>

=
<p>=E5=9F=BA=E6=9C=AC=E5=80=A4=E3=82=92=E5=85=83=E3=81=AB=E3=80=81=E4=BD=BF=
=E7=94=A8=E3=81=97=E3=81=9FBP=E3=81=AE=E9=87=8F=E3=81=AB=E5=BF=9C=E3=81=98=
=E3=81=A6=E7=A2=BA=E7=8E=87=E3=81=8C=E4=BB=A5=E4=B8=8B=E3=81=AE=E6=A7=98=E3=
=81=AB=E5=A4=89=E5=8B=95=E3=81=99=E3=82=8B=E3=80=82</p>

<pre><code>BP1=EF=BC=9A=E5=9F=BA=E6=9C=AC=E5=80=A4=E3=81=AE50%
BP2=EF=BC=9A=E5=9F=BA=E6=9C=AC=E5=80=A4=E3=81=AE10%
BP3=EF=BC=9A=E5=9F=BA=E6=9C=AC=E5=80=A4=E3=81=AE150%
</code></pre>

<p>=E7=B6=99=E7=B6=9A=E7=8E=87=E3=81=AF95%=E3=81=8C=E6=9C=80=E5=A4=A7=E5=80=
=A4=E3=80=82<br>
=
=E3=81=9D=E3=82=8C=E4=BB=A5=E4=B8=8A=E3=81=AE=E5=80=A4=E3=81=AB=E3=81=AA=E3=
=82=8B=E5=A0=B4=E5=90=88=E3=81=AF=E3=80=81=E5=85=A8=E3=81=A695%=E3=81=AB=E6=
=8A=91=E3=81=88=E3=82=89=E3=82=8C=E3=82=8B=E3=80=82</p>

<p>=E5=BE=A9=E6=B4=BB=E3=81=AB=E9=96=A2=E3=81=97=E3=81=A6=E3=81=AF=E4=B8=80=
=E5=BE=8B25%=E3=81=AE=E7=A2=BA=E7=8E=87=E3=81=A7=E7=99=BA=E5=8B=95=E3=80=82=
</p>

<h2>=E6=94=BB=E6=92=83=E6=99=82=E3=81=AE=E3=83=80=E3=83=A1=E3=83=BC=E3=82=B8=
=E3=81=A8=E6=88=90=E5=8A=9F=E7=A2=BA=E7=8E=87=E3=81=AE=E8=A8=88=E7=AE=97=E6=
=96=B9=E6=B3=95</h2>

<h3>=E3=83=80=E3=83=A1=E3=83=BC=E3=82=B8</h3>

<p>=E3=83=80=E3=83=A1=E3=83=BC=E3=82=B8=E5=9F=BA=E6=9C=AC=E5=80=A4=E3=81=AE=
=E7=AE=97=E5=87=BA=E5=BC=8F=E3=81=AF=E4=BB=A5=E4=B8=8B=E3=81=AE=E9=80=9A=E3=
=82=8A=E3=80=82<br>
=E5=B0=8F=E6=95=B0=E7=82=B9=E4=BB=A5=E4=B8=8B=E3=81=AE=E5=80=A4=E3=81=AF=E5=
=88=87=E3=82=8A=E6=8D=A8=E3=81=A6=E3=80=82</p>

<pre><code>=E5=9F=BA=E6=9C=AC=E5=80=A4 =3D =
=E3=83=97=E3=83=AC=E3=82=A4=E3=83=A4=E3=83=BC=E3=81=AE=E6=88=A6=E9=97=98=E5=
=8A=9B^1.6 / =E3=83=9C=E3=82=B9=E3=81=AE=E6=88=A6=E9=97=98=E5=8A=9B^0.6 =
* 0.01
</code></pre>

<p>=E5=9F=BA=E6=9C=AC=E5=80=A4=E3=81=8B=E3=82=89=C2=B120%=E3=81=AE=E3=82=86=
=E3=82=89=E3=81=8E=E3=82=92=E6=8C=81=E3=81=A4=E3=80=82</p>

<pre><code>=E9=80=9A=E5=B8=B8=E3=83=80=E3=83=A1=E3=83=BC=E3=82=B8 =3D =
=E5=9F=BA=E6=9C=AC=E5=80=A4 =C2=B1 20%
</code></pre>

=
<p>=E6=8A=BC=E3=81=97=E9=A0=86=E3=82=A2=E3=83=AA=E3=81=AE=E5=A0=B4=E5=90=88=
=E3=81=AF=E3=80=81=E3=81=95=E3=82=89=E3=81=AB=E3=81=93=E3=81=AE=E5=80=A4=E3=
=81=B830%=E3=81=AE=E3=83=9C=E3=83=BC=E3=83=8A=E3=82=B9=E3=81=8C=E4=BB=98=E4=
=B8=8E=E3=81=95=E3=82=8C=E3=82=8B=E3=80=82</p>

<pre><code>=E3=83=80=E3=83=A1=E3=83=BC=E3=82=B8 =3D =E9=80=9A=E5=B8=B8=E3=83=
=80=E3=83=A1=E3=83=BC=E3=82=B8 + 30%
</code></pre>

<h3>=E6=88=90=E5=8A=9F=E7=8E=87</h3>

<pre><code>=E6=88=90=E5=8A=9F=E7=8E=87 =3D =E3=83=97=E3=83=AC=E3=82=A4=E3=83=
=A4=E3=83=BC=E3=81=AE=E6=88=A6=E9=97=98=E5=8A=9B - =E3=83=9C=E3=82=B9=E3=81=
=AE=E6=88=A6=E9=97=98=E5=8A=9B * 0.003 + 80
</code></pre>

<h2>=E9=98=B2=E5=BE=A1=E6=99=82=E3=81=AE=E3=83=80=E3=83=A1=E3=83=BC=E3=82=B8=
=E3=81=A8=E6=88=90=E5=8A=9F=E7=A2=BA=E7=8E=87=E3=81=AE=E8=A8=88=E7=AE=97=E6=
=96=B9=E6=B3=95</h2>

<h3>=E4=B8=8A=E4=B9=97=E3=81=9B=E5=9B=9E=E6=95=B0</h3>

<p>=E4=B8=8A=E4=B9=97=E3=81=9B=E5=9B=9E=E6=95=B0=E3=81=AE=E7=AE=97=E5=87=BA=
=E5=BC=8F=E3=81=AF=E4=BB=A5=E4=B8=8B=E3=81=AE=E9=80=9A=E3=82=8A=E3=80=82<b=
r>
=E5=B0=8F=E6=95=B0=E7=82=B9=E4=BB=A5=E4=B8=8B=E3=81=AE=E5=80=A4=E3=81=AF=E5=
=88=87=E3=82=8A=E6=8D=A8=E3=81=A6=E3=80=82</p>

<pre><code>=E9=80=9A=E5=B8=B8=E5=9B=9E=E6=95=B0 =3D =
(=E3=83=97=E3=83=AC=E3=82=A4=E3=83=A4=E3=83=BC=E3=81=AE=E6=88=A6=E9=97=98=E5=
=8A=9B - =E3=83=9C=E3=82=B9=E3=81=AE=E6=88=A6=E9=97=98=E5=8A=9B) * =
0.0002 + 3
</code></pre>

<h3>=E6=88=90=E5=8A=9F=E7=8E=87</h3>

<pre><code>=E9=80=9A=E5=B8=B8=E6=88=90=E5=8A=9F=E7=8E=87 =3D =
=E3=83=97=E3=83=AC=E3=82=A4=E3=83=A4=E3=83=BC=E3=81=AE=E6=88=A6=E9=97=98=E5=
=8A=9B - =E3=83=9C=E3=82=B9=E3=81=AE=E6=88=A6=E9=97=98=E5=8A=9B * 0.005 =
+ 60
</code></pre>

=
<p>=E6=8A=BC=E3=81=97=E9=A0=86=E3=82=A2=E3=83=AA=E3=81=AE=E5=A0=B4=E5=90=88=
=E3=81=AF=E3=80=81=E3=81=95=E3=82=89=E3=81=AB=E3=81=93=E3=81=AE=E5=80=A4=E3=
=81=B825%=E3=81=AE=E3=83=9C=E3=83=BC=E3=83=8A=E3=82=B9=E3=81=8C=E4=BB=98=E4=
=B8=8E=E3=81=95=E3=82=8C=E3=82=8B=E3=80=82</p>

<pre><code>=E6=88=90=E5=8A=9F=E7=8E=87 =3D =E9=80=9A=E5=B8=B8=E6=88=90=E5=8A=
=9F=E7=8E=87 + 25%
</code></pre>

<h2>=E3=83=A9=E3=83=83=E3=82=B7=E3=83=A5=E3=81=AE=E3=83=80=E3=83=A1=E3=83=BC=
=E3=82=B8=E3=81=AE=E8=A8=88=E7=AE=97=E6=96=B9=E6=B3=95</h2>

=
<p>=E3=83=A9=E3=83=83=E3=82=B7=E3=83=A5=E6=99=82=E3=81=AE=E3=83=80=E3=83=A1=
=E3=83=BC=E3=82=B8=E3=81=AF=E9=80=9A=E5=B8=B8=E6=94=BB=E6=92=83=EF=BC=88=E6=
=8A=BC=E3=81=97=E9=A0=86=E3=81=AA=E3=81=97=EF=BC=89=E6=99=82=E3=83=80=E3=83=
=A1=E3=83=BC=E3=82=B8=E3=81=AE2=E3=80=9C3=E5=80=8D</p>

<pre><code>=E5=9F=BA=E6=9C=AC=E5=80=A4 =3D =
=E3=83=97=E3=83=AC=E3=82=A4=E3=83=A4=E3=83=BC=E3=81=AE=E6=88=A6=E9=97=98=E5=
=8A=9B^1.6 / =E3=83=9C=E3=82=B9=E3=81=AE=E6=88=A6=E9=97=98=E5=8A=9B^0.6 =
* 0.01
=E9=80=9A=E5=B8=B8=E3=83=80=E3=83=A1=E3=83=BC=E3=82=B8 =3D =E5=9F=BA=E6=9C=
=AC=E5=80=A4 =C2=B1 20%
=E3=83=80=E3=83=A1=E3=83=BC=E3=82=B8 =3D =E9=80=9A=E5=B8=B8=E3=83=80=E3=83=
=A1=E3=83=BC=E3=82=B8 + 100 =E3=80=9C 200%
</code></pre>

</body>
</html>=

--Apple-Mail=_682EF258-D8A0-4E0D-A757-A30ADB69D218
Content-Disposition: inline;
    filename=__.png
Content-Type: image/png;
    x-unix-mode=0644;
    name="__.png"
Content-Transfer-Encoding: base64

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
QmCC

--Apple-Mail=_682EF258-D8A0-4E0D-A757-A30ADB69D218--
"""

    def get_config(self):
        config = ConfigParser.SafeConfigParser()
        config.readfp(StringIO.StringIO(self.config_string))
        return config

    def setUp(self):
        config = sf.AppConfig(StringIO.StringIO(self.config_string))
        self.server = sf.SMTPTriggerServer(config)

    def tearDown(self):
        filepath = os.path.join(rootpath, 'test001')
        os.remove(filepath)

    def test_execute(self):
        from_email = 'hoge@hoge.com'
        to_email = ('test@test001.com',)

        process = self.server.process_message('peer', from_email, to_email, self.mail)
        process.join()

if __name__ == '__main__':
    unittest.main()
