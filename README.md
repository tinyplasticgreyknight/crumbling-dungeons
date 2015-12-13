A random dungeon generator, based almost entirely on a method by Andrew Shields:
* https://fictivefantasies.files.wordpress.com/2013/05/murder-diggers-5-131.pdf
* https://fictivefantasies.files.wordpress.com/2013/05/death-on-ice.pdf

## Invocation
`crumble.py _<input-tables.csv>_ _<random-seed>_`

Probably I'll modify it to pick a random seed if not supplied.

## Output
Output currently includes:
* A layout description file (`graph.dot`) suitable for use as input to graphviz using an invocation like `dot -Tpng graph.dot >graph.png`.
* A room key (`key.md`) with markdown formatting.  This could be converted to something prettier or just viewed directly in a text editor.

## Tables
There is an example of the input table file in the `examples` directory (tweaked slightly from Andrew's original to be more machine-readable).

Note that the "Room exits" roll is currently ignored; instead we start with d6 exits at the initial room, then each of those rooms has d6-1 exits, then d6-2, and so on.  Some rooms are also crosslinked back to each other.  This is a bit easier to automatically generate without having dungeons of unbounded size.

## Templates
Square brackets are used to include templates in

### Dice rolls
Templates of the form `[d6]` or `[2d10]` or `[d12+7]` or `[3d6x100]` will be replaced with the result of the appropriate dice roll.

### Creatures present
Templates which match the name of a row in the Creatures table will be replaced with just that creature's name, and the creature type will be marked as present in this room.

The room's key will include a Stat Blocks section with the stats of every creature type marked as present.

### Tags
An expression of the form `[#tagname]` is removed from the final output, and instead adds to the room's list of tags.  Tags without defined meanings are still included, so you can use these however you like

Tags with defined meanings are:
* `[#trapexit]`: A trap in this room functions as an additional exit, if you're brave enough.  The generator doesn't (yet) assign a connection for this exit, but its existence will be noted in the room's Exits section.

## Statblocks
This method was originally for _Crumbling Epoch_, and the example stats are for that system.  However, the generator is system-agnostic and will reproduce whatever stat tables you put in the input CSV.
