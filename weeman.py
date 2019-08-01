# ! / usr / bin / env python2
# #
# weeman.py - Servidor HTTP para phishing
# #
#   Weeman es software libre; puedes redistribuirlo y / o modificarlo
#   bajo los términos de la Licencia Pública General de GNU publicada por
#   la Fundación para el Software Libre; ya sea la versión 2 de la Licencia, o
#   (a su elección) cualquier versión posterior.
# #
#   Weeman se distribuye con la esperanza de que sea útil,
#   pero SIN NINGUNA GARANTÍA; sin siquiera la garantía implícita de
#   COMERCIABILIDAD o APTITUD PARA UN PROPÓSITO EN PARTICULAR. Ver el
#   GNU General Public License para más detalles.
# #
#   Debería haber recibido una copia de la Licencia Pública General de GNU
#   junto con este programa. Si no, vea <http://www.gnu.org/licenses/>.
# #
# Copyright (C) 2015 Hypsurus <hypsurus@mail.ru>
# #

importación sys
importar optparse
de core.misc import printt
desde core.config import user_agent como usera

def  tests_pyver ():
    si sys.version [: 3 ] ==  " 2.7 "  o  " 2 "  en sys.version [: 3 ]:
        pase  # todo bien
    elif  " 3 "  en sys.version [: 3 ]:
        printt ( 1 , " Weeman no tiene soporte para Python 3. " )
    más :
        printt ( 1 , " Su versión de Python es muy antigua .. " )

def  tests_platform ():
    si  " linux "  en sys.platform:
        # printt (3, "Ejecutando Weeman en Linux ... (Todo bien)")
        pasar
    elif  " darwin "  en sys.platform:
        # printt (3, "Ejecutando Weeman en \ 'Mac \' (Todo bien)")
        pasar
    elif  " win "  en sys.platform:
        print ( " Lo siento, no hay soporte para windows en este momento " )
        sys.exit ( 1 )
    más :
        printt ( 3 , " Si \ ' Weeman \' se ejecuta con éxito en su plataforma % s \ n ¡ Avíseme (@Hypsurus)! "  % sys.platform)

def  main ():
    tests_pyver ()
    tests_plataforma ()
    analizador = optparse.OptionParser ()
    parser.add_option ( " -q " , " --quiet " , dest = " quiet_mode_opt " , action = " store_true " , default = False , help = " Se ejecuta sin mostrar el banner " . )
    parser.add_option ( " -p " , " --profile " , dest = " profile " , help = " Cargar perfil weeman " . )
    opciones, r = parser.parse_args ()

    if options.profile:
        desde core.shell import shell_noint
        shell_noint (options.profile)
    más :
        desde core.shell import shell
        cáscara()

if  __name__  ==  ' __main__ ' :
    principal()
