import types
import random
import sys
import _pickle
import ast
# from namer import main as namer
# from if_obf import IfObf

nm = []
def genPref() -> str:
    while (_nm:=''.join(random.choices('FAGHPNDSEW', k=4)))in nm:0
    nm.append(_nm)
    return _nm

def genName() -> str:
    while (_nm:='_0x'+''.join(random.choices('QWERTYUIOPASDFGHJKLLZXCVBNM', k=10)))in nm:0
    nm.append(_nm)
    return _nm

def oStr(text):
    is_bytes = isinstance(text,bytes)
    encoded_chars = []
    for char in text[::-1]:
        val = char if is_bytes else ord(char)
        if val % 2 == 0 and (val // 2) <= 60:
            encoded_chars.append(val // 2)
        else:
            encoded_chars.append(val)

    fmt_str = "%c" * len(text)
    tuple_str = "(" + ", ".join(map(str, encoded_chars)) + ("," if len(encoded_chars) == 1 else "") + ")"
    obfuscated = f'{'b'if is_bytes else''}"{fmt_str}" % tuple(map(lambda mvk__: (mvk__)*2 if mvk__ <= 60 else (mvk__) if mvk__ > 1 else {'bytes'if is_bytes else'chr'}({genPref()}), {tuple_str}))[::-1]'
    
    return obfuscated


def makeatypes(c: types.CodeType) -> str:
    consts_pool = []
    consts_map = {}

    _Tr = genPref().encode()
    _Fl = genPref().encode()
    _No = genPref().encode()
    _st = genPref().encode()
    _i = genPref().encode()
    _i2 = genPref().encode()
    _imp = genPref().encode()
    def constttt(cc):
        aa = cc
        if isinstance(cc, str):
            aa = bytearray()
            for cr in cc.encode():
                cr *= 5
                cr += 17
                cr &= 255
                aa.append(cr)
            aa = _st + aa
        elif isinstance(cc, type(None)):
            aa = _No # None
        elif isinstance(cc, bool):
            if cc: aa = _Tr # True
            else: aa = _Fl # False
        return aa

    _dc = genName()
    def get_idx(val):
        key = (type(val), val)
        if key not in consts_map:
            consts_map[key] = len(consts_pool)
            consts_pool.append(constttt(val))
        return f"{_dc}(__CONST__[{consts_map[key]}])"

    def format_tuple(tup):
        if not tup:
            return "()"
        elements = []
        for item in tup:
            if isinstance(item, types.CodeType):
                elements.append(build_code_obj_str(item))
            elif isinstance(item, tuple):
                elements.append(format_tuple(item))
            else:
                elements.append(get_idx(item))
                
        return f"({', '.join(elements)}{',' if len(elements) == 1 else ''})"

    run = genName()
    def build_code_obj_str(o: types.CodeType) -> str:
        if sys.version_info >= (3, 11):
            return f"""{run}(
    {get_idx(o.co_argcount)}, {get_idx(o.co_posonlyargcount)}, {get_idx(o.co_kwonlyargcount)}, {get_idx(o.co_nlocals)},
    {get_idx(o.co_stacksize)}, {get_idx(o.co_flags)}, {get_idx(o.co_code)}, {format_tuple(o.co_consts)},
    {format_tuple(o.co_names)}, {format_tuple(o.co_varnames)}, {get_idx('')},
    {get_idx('')}, {get_idx('')},
    {get_idx(-9999)}, {get_idx(b'')},
    {get_idx(getattr(o, 'co_exceptiontable', b''))}, {format_tuple(o.co_freevars)}, {format_tuple(o.co_cellvars)}
)"""
        else:
            return f"""{run}(
    {get_idx(o.co_argcount)}, {get_idx(getattr(o, 'co_posonlyargcount', 0))}, {get_idx(o.co_kwonlyargcount)},
    {get_idx(o.co_nlocals)}, {get_idx(o.co_stacksize)}, {get_idx(o.co_flags)}, {get_idx(o.co_code)},
    {format_tuple(o.co_consts)}, {format_tuple(o.co_names)}, {format_tuple(o.co_varnames)},
    {get_idx(o.co_filename)}, {get_idx(o.co_name)}, {get_idx(o.co_firstlineno)},
    {get_idx(getattr(o, 'co_lnotab', b''))}, {format_tuple(o.co_freevars)}, {format_tuple(o.co_cellvars)}
)"""
        
    mega_expr = build_code_obj_str(c)
    n = rf'''
def {run}():__doc__='huy'
{run}=type({run}.__code__)
({(aga:=genName())}:=(lambda:0)).{(__i:=genName())} = vars(__builtins__)[{oStr('isinstance')}]
({(aga1:=genName())}:=(lambda:0)).{(__i1:=genName())} = vars(__builtins__)[{oStr('getattr')}]
{(____asd:=genName())} = {{
    {oStr(_i)}: {aga}.{__i},
    {oStr(_i2)}: {aga1}.{__i1},
    {oStr(_No)}: lambda {(x1:=genName())}: ([None]*len({x1}.decode()))[0],
    {oStr(_Tr)}: lambda {(x2:=genName())}: {____asd}[{oStr(_i)}]({x2},type(b'\x00')),
    {oStr(_Fl)}: lambda {(x3:=genName())}: not {____asd}[{oStr(_i)}]({x3},type(b'\x00'))
}}
{____asd}[{oStr(_imp)}] = vars({____asd}[{oStr(_i2)}]({____asd}[{oStr(_i)}], {oStr('__self__')}))[{oStr('__import__')}]

def {_dc}({(_cc:=genName())}):
    if {____asd}[{oStr(_i)}]({_cc},type({____asd}[{oStr(_i2)}](KeyError,{oStr('__sizeof__')})(eval({oStr('print')})))):
        return {_cc}
    elif {oStr(_st)} in {_cc}:
        {(_aa:=genName())} = str()
        for {(_cr:=genName())} in {_cc}[4:]:
            {_cr} -= 17
            {_cr} *= 205
            {_cr} &= 255
            {_aa} += chr({_cr})
        return {_aa}
    else:
        if {____asd}[{oStr(_i)}](({(asddd:=genName())}:={____asd}.get({_cc}, {_cc})), type(lambda:0)):
            return {asddd}({_cc})
        else: return {_cc}
{(t:=genName())} = {____asd}[{oStr(_i2)}]({____asd}[{oStr(_i2)}]({____asd}[{oStr(_i2)}]({____asd}[{oStr(_imp)}]({oStr('sys')}), {oStr('_getframe')})(0), {oStr('f_code')}), {oStr('co_linetable')})
{(tt:=genName())} = {____asd}[{oStr(_i2)}]({____asd}[{oStr(_imp)}]({oStr('_pickle')}), {oStr('loads')})
({(__a:=genName())}:=({(___b:=genName())}:=dict)()).update({___b}(globals()))
type(lambda:'huy')({mega_expr}, {__a})()
'''.replace('__CONST__', f'{tt}({t}[-{len(_pickle.dumps(consts_pool))}:])')
    globals()['constsss'] = consts_pool
    # return IfObf(namer(n, False))
    return n

def BoBo(co: types.CodeType) -> types.CodeType:
    isspec = co.co_name == loaderName
    new_consts: list = []
    for const in co.co_consts:
        if isinstance(const, types.CodeType):
            new_consts.append(BoBo(const))
        else:
            new_consts.append(const)
    return co.replace(
        co_consts=tuple(new_consts),
        co_name = co.co_name if isspec else'',
        co_qualname = '',
        co_linetable = b'\x02'+_pickle.dumps(constsss) if isspec else b'',
        co_firstlineno = 0,
        co_filename = ''
        )

loaderName = genName()

code = f"""
def _rr(co, of, k):
    if not isinstance(co, (cc:=type(compile('','',{oStr('exec')})))) or co.co_name == {oStr(loaderName)}:
        return co
    rc = list(co.co_code)
    if of:
        for ko, ofs in of.items():
            if ko == {oStr('c')}: 
                continue
            oc = int(ko)
            for off in ofs:
                rc[off] = oc
    nc = []
    cs = of.get({oStr('c')}, {{}}) if of else {{}}
    for i, c in enumerate(co.co_consts):
        if isinstance(c, bytes):
            try:
                nc.append(bytes([c[j] ^ k[j % len(k)] for j in range(len(c))]).decode())
            except:
                nc.append(c)
        elif isinstance(c, type(213)) and c != 0:
            nc.append(c - 234432)
        elif isinstance(c, cc):
            cp = cs.get(i, None)
            nc.append(_rr(c, cp, k))
        else:
            nc.append(c)
    return co.replace(co_code=bytes(rc), co_consts=tuple(nc))
if not getattr(__file__, {oStr('endswith')})({oStr('.pyc')}): 
    print({oStr('nope: .pyc')})
    getattr(__import__({oStr('sys')}), 'exit')()
    raise
try:
    (s:=__import__({oStr('sys')}))._getframe(6).f_code
    getattr(s, {oStr('exit')})()
    raise
except ValueError:
    if not hasattr(s, '_pizdec'):
        setattr(s,{oStr('_pizdec')},True)
        d = _rr(s._getframe(2).f_code, __MAP__, __KEY__)
        type(lambda: None)(d, globals())()
        getattr(s, {oStr('exit')})()
"""


source = open('tester.py', 'r', errors='ignore', encoding='utf8').read()


key = b'\x98\xcc\xe9\xf0\xe0\xc7\xb4\xef\x11\xe1\xf2\x9f\x8c\x94\x83\xa2\xdf\xbd'

def xor_data(data, key):
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])
    
def obf_int(i):
    return i + 234432


children = genName()
template = fr"""
def {loaderName}():
    __FUNC__
{loaderName}()


{source}
"""

def process_code_recursive(co, key):
    if not isinstance(co, types.CodeType) or co.co_name == loaderName:
        return co, None

    raw_code = list(co.co_code)
    target_opcodes = {
        101, 100, 116, 106, 95, 124, 122, 114, 126, 172, 134, 
        115, 135, 121, 143, 93, 138, 140, 108, 109, 125, 90,
        83, 92
    }
    current_map = {str(op): [] for op in target_opcodes}
    
    start_offset = 20 if co.co_name == '<module>' else 0
    jo = [
        1,2,4,5,9,11,12,15,30,31,32,33,36,37,
        128,172,245,149,
        # 115, 79, 116, 84
    ]
    for i in range(start_offset, len(raw_code)):
        byte = raw_code[i]
        if byte in target_opcodes:
            current_map[str(byte)].append(i)
            raw_code[i] = random.choice(jo)


    new_consts = []
    children_map = {}
    
    for i, const in enumerate(co.co_consts):
        if isinstance(const, str):
            new_consts.append(xor_data(const.encode(), key))
        elif isinstance(const, int) and const != 0:
            new_consts.append(obf_int(const))
        elif isinstance(const, types.CodeType):
            new_child_co, child_map = process_code_recursive(const, key)
            new_consts.append(new_child_co)
            if child_map:
                children_map[i] = child_map
        else:
            new_consts.append(const)
            
    new_co = co.replace(co_code=bytes(raw_code), 
                        co_consts=tuple(new_consts),
                        co_firstlineno = 1,
                        co_linetable = b'',
                        co_filename='',
                        co_name='',
                        co_qualname='' 
                        )
    
    current_map['c'] = children_map
    
    return new_co, current_map

def wP(co, file = 'obf.pyc'):
    import importlib._bootstrap_external as imp_b
    open(file, 'wb').write(imp_b._code_to_timestamp_pyc(co))

temp_obj = compile(template, '', 'exec')
# from PYCDAS import dis
# dis(temp_obj, file='dis.txt')

final_code_obj, full_map = process_code_recursive(temp_obj, key)

# co = BoBo(compile(makeatypes(BoBo(compile(code.replace('__MAP__', str(full_map)).replace('__KEY__', str(key)).replace('__children__', children),'','exec'))), '', 'exec'))
# co = co.replace(co_linetable=b'\x02'+_pickle.dumps(constsss))
# _enc = imp_b._code_to_timestamp_pyc(co)
# open('ESHKERE.pyc', 'wb').write(_enc)
# enc_loader = makeatypes(BoBo(compile(IfObf(namer(code.replace('__MAP__', str(full_map)).replace('__KEY__', str(key)).replace('__children__', children), False)),'','exec')))
enc_loader = makeatypes(BoBo(compile(code.replace('__MAP__', str(full_map)).replace('__KEY__', str(key)).replace('__children__', children),'','exec')))
tr = ast.unparse(ast.FunctionDef(loaderName,[],ast.parse(enc_loader).body,[],lineno=0))

final_source = template.replace(f'''def {loaderName}():
    __FUNC__''', tr)
# open('loaderrr.py', 'w', encoding='utf8').write(final_source)
final_code_obj_with_map = compile(final_source, '', 'exec')

final_ready_code, _ = process_code_recursive(final_code_obj_with_map, key)

wP(BoBo(final_ready_code), 'tester_obf.pyc')

