wx_data = eval('('+wx_data+')');
document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_ddlAPP_NATL').value = wx_data.p2_01;
setDirty();
setTimeout('__doPostBack(\'ctl00$SiteContentPlaceHolder$FormView1$ddlAPP_NATL\',\'\')', 0)
if (wx_data.p2_02 == 1) {
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_rblAPP_OTH_NATL_IND_0').checked = true;
	setDirty();
	setTimeout('__doPostBack(\'ctl00$SiteContentPlaceHolder$FormView1$rblAPP_OTH_NATL_IND$0\',\'\')', 0)
} else {
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_rblAPP_OTH_NATL_IND_1').checked = true;
	setDirty();
}
if (wx_data.p2_02 == 1) {
	// TODO Other Nationality
}
if (wx_data.p2_03 == 1) {
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_rblPermResOtherCntryInd_0').checked = true;
	setDirty();
	setTimeout('__doPostBack(\'ctl00$SiteContentPlaceHolder$FormView1$rblPermResOtherCntryInd$0\',\'\')', 0)
} else {
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_rblPermResOtherCntryInd_1').checked = true;
	setDirty();
}
if (wx_data.p2_03 == 1) {
	// TODO Other Nationality
}
if (wx_data.p2_04 == "") {
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_cbxAPP_NATIONAL_ID_NA').checked = true;
	setDirty();
	enableTbx('ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_NATIONAL_ID', 'ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_NATIONAL_ID_NA');
} else {
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_NATIONAL_ID').value = wx_data.p2_04;
	setDirty();
}
if (wx_data.p2_05 == "" || wx_data.p2_06 == "" || wx_data.p2_07 == "") {
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_cbxAPP_SSN_NA').checked = true;
	setDirty();
	enableTbx3('ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_SSN1', 'ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_SSN2','ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_SSN3','ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_SSN_NA');
} else {
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_SSN1').value = wx_data.p2_05;
	setDirty();
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_SSN2').value = wx_data.p2_06;
	setDirty();
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_SSN3').value = wx_data.p2_07;
	setDirty();
}
if (wx_data.p2_08 == "") {
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_cbxAPP_TAX_ID_NA').checked = true;
	setDirty();
	enableTbx('ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_TAX_ID', 'ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_TAX_ID_NA');
} else {
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_TAX_ID').value = wx_data.p2_08;
	setDirty();
}
document.getElementById('ctl00_SiteContentPlaceHolder_UpdateButton3').click();



