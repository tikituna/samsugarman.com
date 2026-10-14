#!/usr/bin/env python3
"""Draws images/valley-map.svg: a 1950s road-map plate of the San Fernando Valley.
Plain equirectangular projection; the same constants are used by valley.html to place the dot."""
import math
LON0, LON1 = -118.665, -118.255   # west, east
LAT0, LAT1 = 34.095, 34.345       # south, north
W = 900
H = round(W * (LAT1-LAT0) / ((LON1-LON0) * math.cos(math.radians(34.22))))
def P(lat, lon):
    return (round((lon-LON0)/(LON1-LON0)*W,1), round((LAT1-lat)/(LAT1-LAT0)*H,1))
def path(pts, **kw):
    d="M"+" L".join(f"{x},{y}" for x,y in (P(a,b) for a,b in pts))
    attrs=" ".join(f'{k.replace("_","-")}="{v}"' for k,v in kw.items())
    return f'<path d="{d}" fill="none" {attrs}/>'
def poly(pts, **kw):
    d="M"+" L".join(f"{x},{y}" for x,y in (P(a,b) for a,b in pts))+" Z"
    attrs=" ".join(f'{k.replace("_","-")}="{v}"' for k,v in kw.items())
    return f'<path d="{d}" {attrs}/>'

# --- geography (approximate, good to a few hundred metres) ---
US101=[(34.135,-118.665),(34.146,-118.640),(34.160,-118.615),(34.172,-118.590),(34.176,-118.560),(34.172,-118.530),(34.160,-118.500),(34.156,-118.470),(34.154,-118.440),(34.148,-118.410),(34.142,-118.385),(34.139,-118.368)]
US101S=[(34.139,-118.368),(34.128,-118.358),(34.112,-118.345),(34.100,-118.335)]      # Cahuenga Pass
SR134=[(34.139,-118.368),(34.145,-118.350),(34.152,-118.330),(34.155,-118.300),(34.153,-118.260)]
I405=[(34.095,-118.470),(34.115,-118.472),(34.135,-118.470),(34.157,-118.469),(34.190,-118.470),(34.230,-118.470),(34.262,-118.472),(34.285,-118.480),(34.305,-118.492),(34.320,-118.498)]
SR170=[(34.148,-118.392),(34.165,-118.399),(34.195,-118.401),(34.222,-118.404)]
I5=[(34.120,-118.280),(34.150,-118.302),(34.180,-118.322),(34.205,-118.355),(34.222,-118.404),(34.250,-118.430),(34.275,-118.455),(34.300,-118.478),(34.322,-118.492),(34.345,-118.505)]
SR118=[(34.272,-118.665),(34.270,-118.620),(34.272,-118.560),(34.274,-118.500),(34.275,-118.470),(34.278,-118.440),(34.282,-118.425)]
I210=[(34.325,-118.470),(34.300,-118.440),(34.282,-118.425),(34.262,-118.385),(34.250,-118.345),(34.245,-118.300),(34.230,-118.260)]
VENTURA=[(34.168,-118.610),(34.171,-118.585),(34.168,-118.560),(34.163,-118.530),(34.158,-118.500),(34.153,-118.470),(34.151,-118.440),(34.145,-118.410),(34.141,-118.390),(34.139,-118.376)]
MULHOLLAND=[(34.108,-118.640),(34.118,-118.600),(34.127,-118.560),(34.124,-118.520),(34.131,-118.480),(34.128,-118.450),(34.126,-118.420),(34.130,-118.390),(34.127,-118.365),(34.115,-118.345)]
RIVER=[(34.202,-118.620),(34.195,-118.580),(34.186,-118.540),(34.180,-118.505),(34.172,-118.480),(34.160,-118.455),(34.150,-118.420),(34.143,-118.390),(34.148,-118.365),(34.155,-118.335),(34.153,-118.305),(34.140,-118.280),(34.120,-118.265)]
TUJUNGA=[(34.262,-118.400),(34.235,-118.398),(34.200,-118.397),(34.170,-118.396),(34.150,-118.395)]
BASIN=[(34.170,-118.508),(34.190,-118.512),(34.197,-118.492),(34.188,-118.470),(34.168,-118.472),(34.164,-118.490)]
LAKE=[(34.183,-118.502),(34.187,-118.496),(34.183,-118.491),(34.177,-118.493),(34.177,-118.500)]
VNY=[(34.197,-118.495),(34.226,-118.494),(34.226,-118.485),(34.197,-118.486)]
BUR=[(34.193,-118.365),(34.207,-118.365),(34.207,-118.350),(34.193,-118.350)]
# hills: south ridge, north ranges, Verdugos, Simi Hills (west)
SOUTH=[(34.095,-118.665),(34.120,-118.640),(34.132,-118.600),(34.138,-118.560),(34.135,-118.520),(34.140,-118.480),(34.137,-118.450),(34.134,-118.420),(34.136,-118.390),(34.132,-118.370),(34.122,-118.350),(34.112,-118.330),(34.100,-118.300),(34.095,-118.255)]
NORTH=[(34.345,-118.665),(34.300,-118.660),(34.292,-118.620),(34.290,-118.580),(34.295,-118.540),(34.300,-118.510),(34.318,-118.480),(34.335,-118.455),(34.345,-118.430)]
VERDUGO=[(34.195,-118.300),(34.215,-118.320),(34.235,-118.330),(34.250,-118.310),(34.245,-118.280),(34.225,-118.260),(34.205,-118.258),(34.190,-118.275)]
SIMI=[(34.345,-118.665),(34.300,-118.660),(34.262,-118.655),(34.235,-118.640),(34.215,-118.635),(34.190,-118.645),(34.160,-118.650),(34.135,-118.665)]
TOWNS=[("CHATSWORTH",34.257,-118.600),("NORTHRIDGE",34.231,-118.537),("GRANADA HILLS",34.282,-118.522),("SYLMAR",34.308,-118.449),("SAN FERNANDO",34.284,-118.436),("PACOIMA",34.260,-118.418),("SUN VALLEY",34.220,-118.370),("BURBANK",34.178,-118.312),("NORTH HOLLYWOOD",34.176,-118.381),("STUDIO CITY",34.158,-118.402),("SHERMAN OAKS",34.164,-118.452),("ENCINO",34.168,-118.504),("TARZANA",34.183,-118.553),("WOODLAND HILLS",34.181,-118.606),("CANOGA PARK",34.203,-118.598),("RESEDA",34.203,-118.536),("VAN NUYS",34.189,-118.449),("PANORAMA CITY",34.228,-118.447),("TOLUCA LAKE",34.154,-118.348),("UNIVERSAL CITY",34.131,-118.350),("MISSION HILLS",34.256,-118.483)]
RED="#b8312f"; INK="#1d1d1d"; PAPER="#f3ecd9"; HILL="#d8ccae"; WATER="#6f9bbf"
out=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Times New Roman, Times, serif">',
 '<defs><pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="6" stroke="#b9a98a" stroke-width="1"/></pattern></defs>',
 f'<rect width="{W}" height="{H}" fill="{PAPER}"/>']
for shape in (SOUTH,NORTH,VERDUGO,SIMI):
    out.append(poly(shape, fill=HILL)); out.append(poly(shape, fill="url(#hatch)", stroke="#a99774", stroke_width="0.8"))
out.append(poly(BASIN, fill="#e3e9d5", stroke="#9bb07a", stroke_width="0.8", stroke_dasharray="3 2"))
out.append(poly(LAKE, fill=WATER, stroke="#4a6f8e", stroke_width="0.6"))
out.append(path(RIVER, stroke=WATER, stroke_width="2", stroke_linejoin="round", stroke_linecap="round"))
out.append(path(TUJUNGA, stroke=WATER, stroke_width="1.4", stroke_linejoin="round", stroke_dasharray="6 3"))
for ap,name,dx in ((VNY,"VAN NUYS AIRPORT",0),(BUR,"BURBANK AIRPORT",0)):
    out.append(poly(ap, fill="#e6e0cc", stroke=INK, stroke_width="0.8"))
out.append(path(MULHOLLAND, stroke=INK, stroke_width="1", stroke_dasharray="4 2"))
out.append(path(VENTURA, stroke=INK, stroke_width="1.6"))
for hw in (US101,US101S,SR134,I405,SR170,I5,SR118,I210):
    out.append(path(hw, stroke=PAPER, stroke_width="5.5", stroke_linejoin="round", stroke_linecap="round"))
for hw in (US101,US101S,SR134,I405,SR170,I5,SR118,I210):
    out.append(path(hw, stroke=RED, stroke_width="2.6", stroke_linejoin="round", stroke_linecap="round"))
def shield(lat,lon,label):
    x,y=P(lat,lon); return f'<g><rect x="{x-11}" y="{y-8}" width="22" height="16" rx="3" fill="{PAPER}" stroke="{RED}" stroke-width="1.2"/><text x="{x}" y="{y+4.2}" text-anchor="middle" font-size="10.5" font-weight="bold" fill="{RED}">{label}</text></g>'
for lat,lon,l in ((34.176,-118.575,"101"),(34.118,-118.351,"101"),(34.215,-118.471,"405"),(34.185,-118.401,"170"),(34.260,-118.440,"5"),(34.165,-118.316,"5"),(34.273,-118.580,"118"),(34.152,-118.318,"134"),(34.250,-118.345,"210")):
    out.append(shield(lat,lon,l))
def label(text,lat,lon,size=11,anchor="middle",style="",fill=INK):
    x,y=P(lat,lon); return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" letter-spacing="1.2" fill="{fill}" {style}>{text}</text>'
for name,lat,lon in TOWNS: out.append(label(name,lat,lon,10.5))
out.append(label("VENTURA BOULEVARD",34.1655,-118.545,8.5,style='font-style="italic"'))
out.append(label("MULHOLLAND DRIVE",34.117,-118.515,8.5,style='font-style="italic"'))
out.append(label("LOS ANGELES RIVER",34.192,-118.560,8,style='font-style="italic"',fill="#4a6f8e"))
out.append(label("SEPULVEDA BASIN",34.180,-118.480,8,fill="#5e7a40"))
out.append(label("SANTA MONICA MOUNTAINS",34.105,-118.560,10,style='font-style="italic"',fill="#6b5b3e"))
out.append(label("SAN GABRIEL MOUNTAINS",34.330,-118.520,10,style='font-style="italic"',fill="#6b5b3e"))
out.append(label("VERDUGO MTNS",34.232,-118.292,8.5,style='font-style="italic"',fill="#6b5b3e"))
out.append(label("SANTA SUSANA MTNS",34.300,-118.620,8.5,style='font-style="italic"',fill="#6b5b3e"))
# cartouche, scale, compass
cx,cy=P(34.322,-118.318)
out.append(f'<g><rect x="{cx-120}" y="{cy-22}" width="240" height="44" fill="{PAPER}" stroke="{INK}" stroke-width="1"/><rect x="{cx-116}" y="{cy-18}" width="232" height="36" fill="none" stroke="{INK}" stroke-width="0.5"/><text x="{cx}" y="{cy-3}" text-anchor="middle" font-size="15" font-weight="bold" letter-spacing="3" fill="{INK}">THE SAN FERNANDO VALLEY</text><text x="{cx}" y="{cy+13}" text-anchor="middle" font-size="9" letter-spacing="2" fill="{INK}">LOS ANGELES COUNTY, CALIFORNIA</text></g>')
# scale bar: 5 miles
mi=5/69.0/math.cos(math.radians(34.22))  # degrees of longitude for 5 miles
sx0,sy=P(34.112,-118.345); sx1,_=P(34.112,-118.345+mi)
out.append(f'<g stroke="{INK}" fill="{INK}"><line x1="{sx0}" y1="{sy}" x2="{sx1}" y2="{sy}" stroke-width="2"/><line x1="{sx0}" y1="{sy-4}" x2="{sx0}" y2="{sy+4}"/><line x1="{sx1}" y1="{sy-4}" x2="{sx1}" y2="{sy+4}"/><text x="{(sx0+sx1)/2}" y="{sy-6}" text-anchor="middle" font-size="8.5" stroke="none" letter-spacing="1">5 MILES</text></g>')
nx,ny=P(34.135,-118.268)
out.append(f'<g fill="{INK}"><polygon points="{nx},{ny-18} {nx-5},{ny+4} {nx},{ny} {nx+5},{ny+4}"/><text x="{nx}" y="{ny-22}" text-anchor="middle" font-size="9" font-weight="bold">N</text></g>')
out.append(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" fill="none" stroke="{INK}" stroke-width="1"/>')
out.append('</svg>')
open('images/valley-map.svg','w').write("\n".join(out))
print("wrote images/valley-map.svg", W, "x", H)
print("JS constants: LON0=%s LON1=%s LAT0=%s LAT1=%s W=%s H=%s" % (LON0,LON1,LAT0,LAT1,W,H))
