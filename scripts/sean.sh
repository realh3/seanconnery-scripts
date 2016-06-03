#!/bin/bash
OUT=`mysql -N -u seanconnery eggdrop -e  'SELECT phrase FROM phrases ORDER BY RAND() limit 1;'`;
echo $OUT;
