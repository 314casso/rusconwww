# $Id: mailto.p, v 1.05 2006/01/17 11:28:00 ������ ����� [wonder@nightmail.ru] Exp $
#      ������� ������� Slash � Misha v.3
@CLASS
mailto


# ����� ������� ���������� ��� email
@print[email;params;type][params;data;_string;_encoded;i;_random]
$data[^hash::create[]]
$data.title[$email]
^if($params is "hash"){
	$data.subject[$params.subject]
	$data.attributes[$params.attributes]
	^if(def $params.title){
		$data.title[$params.title]
	}
}
^if($params is "string" && def $params){
	$data.title[$params]
}

^rem{ *** ��������� ���������� ����������� ������ *** }
^if(^email.pos[@] > 0 && ^email.match[^^\w+([.-]?\w+)+\@\w+([.-]?\w+)*\.[a-z]{2,4}^$][i]){
	$_string[<a href="mailto:$email^if(def $data.subject){?subject=^taint[uri][$data.subject]}"^if(def $data.attributes){ $data.attributes}>$data.title</a>]
}{
	$_string[$email]
}

^rem{ *** ������� ������ *** }
$i(0)
^while($i < ^_string.length[]){
	$_random(^math:random(5) + 3)
	$_encoded[$_encoded^_string.mid($i;$_random)^if($i + $_random < ^_string.length[]){'+'}]
	^i.inc($_random)
}

^rem{ *** ���������� ��������� � ����������� �� $type *** }
^switch[$type]{
	^case[xml]{
		$result[<email-crypted>^taint[xml][$_encoded]</email-crypted>]
	}
	^case[html;DEFAULT]{
		$result[<script type="text/javascript">document.write('$_encoded')</script>]
	}
}
# end @print[]


# ����� ������� ��� email � ���������� ������
@crypt[body;type]
$result[^body.match[<(a) href=["']mailto:(.+?)(\?subject=(.+?))?["'](.*?)>(.+?)</\1>][gi]{
	^self.print[$match.2][
		$.title[$match.6]
		$.subject[$match.4]
		$.attributes[$match.5]
	][$type]
}]
# end @crypt[]