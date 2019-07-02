AOS.init();

var dropdownNames = ['dropdown_reserve',
                    'dropdown_hamburguer',
                    'dropdown_language_hamburguer',
                    'dropdown_language']
for (dropdownName of dropdownNames) {
  dropdown = initDivMouseOver(dropdownName);
  button = initDivMouseOver(dropdownName + '_button');
  dropdowns.push([dropdown, button])
}
