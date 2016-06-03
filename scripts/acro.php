#!/usr/bin/env php
<?php
// author: ian

//echo "input: " . $argv[1] . "\n";

//$raw_input_array = explode( " ", $argv[1] );
//print_r( $argv );
if( $argv[1] == "TheManticore" ) {
	array_shift($argv);
	$argl = array();

	for($i = 0; $i < count($argv); $i++) {
		if ( strpos($argv[$i], " ") != -1 ) {
			$arr = split(" ", $argv[$i]);
			for ($j = 0; $j < count($arr); $j++) {
				array_push($argl, $arr[$j]);
			}
		} else {
			array_push($argl, $argv[$i]);
		}
	}

	$filtered_input_array = preg_grep( "/^[A-Z]{2,6}$/", $argl );


	foreach( $filtered_input_array as $acronym ) {
	    $html = file_get_contents( "http://acronyms.thefreedictionary.com/$acronym" );
	    preg_match( "@<td class=acr>[A-Z]{2,5}</td><td>(.*?)</td>@", $html, $matches );

	    if( $matches ) {
		echo "$acronym: " . strip_tags( $matches[1] );
	    }
	    else {
		echo "$acronym: Oh god I have no idea! What is internet?";
	    }

	    echo "  ";
	}
}
