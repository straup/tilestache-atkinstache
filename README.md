Atkinstache
--

Atkinstache is a [TileStache]() provider for generating stylized black and white
halftone, or "dithered", map tiles using another tileset as its input. The
halftone effect is accomplished using Bill Atkinson's original dithering
algorithm created for the first Apple Macintosh computers.

Typically you would use satellite imagery but there's nothing to stop you from
using a different source.

How to
--

It exposes a single provider named `atkinstache.dithering.Provider` and you
invoke it in your TileStache config like this:

	"layers": {
		"microsoft_aerial": {
			"provider": { "name": "proxy", "provider": "MICROSOFT_AERIAL" }
		},

		"dithering": {
			"provider": {
				"class": "atkinstache.dithering.Provider",
				"kwargs": {
					"source_layer": "microsoft_aerial",
					"skip_on_checksum": "1",
					"checksum": "afeeb6c8b0a5edb1b9ef94d1d652f41b"
				}
			}
		}
	}

If the `skip_on_checksum` flag is true then the contents of each new tile (from
the `source_layer` provider) will be MD5 hashed and compared to the `checksum`
value. If the two match the tile will not be dithered. You might want to do this
for tile sets that send a unique tile for those areas that lack coverage.

Other stuff
--

**this part does not work yet**

By default Atkinstache will use a pure Python implementation of the dithering
algorithm to filter images. If the C-based (atk)[] Python implimentation is
installed the package will use that instead.

See also:

* [TileStache]()

* [atk]()

* [](http://mike.teczno.com/notes/atkinson.html)
