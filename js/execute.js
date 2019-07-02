AOS.init();

var dropdownNames = ['dropdown_reserve',
                    'dropdown_hamburguer',
                    'dropdown_language_hamburguer',
                    'dropdown_language']

for (dropdownName of dropdownNames) {
  initDivMouseOver(dropdownName);
  initDivMouseOver(dropdownName + '_button');
}
