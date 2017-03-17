wx_data = eval('('+wx_data+')');
document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_ADDR_LN1').value = wx_data.p3_01;
setDirty();
document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_ADDR_LN2').value = wx_data.p3_02;
setDirty();
document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_ADDR_CITY').value = wx_data.p3_03;
setDirty();
if (wx_data.p3_04 == "") {
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_cbxAPP_ADDR_STATE_NA').checked = true;
	setDirty();
	enableTbx('ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_ADDR_STATE','ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_ADDR_STATE_NA');
} else {
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_ADDR_STATE').value = wx_data.p3_04;
	setDirty();
}
if (wx_data.p3_05 == "") {
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_cbxAPP_ADDR_POSTAL_CD_NA').checked = true;
	setDirty();
	enableTbx('ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_ADDR_POSTAL_CD','ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_ADDR_POSTAL_CD_NA');
} else {
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_ADDR_POSTAL_CD').value = wx_data.p3_05;
	setDirty();
}
document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_ddlCountry').value = wx_data.p3_06;
setDirty();
if (wx_data.p3_07 == 1) {
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_rblMailingAddrSame_0').checked = true;
	setDirty();
	setTimeout('__doPostBack(\'ctl00$SiteContentPlaceHolder$FormView1$rblMailingAddrSame$0\',\'\')', 0);
} else {
	setDirty();
	setTimeout('__doPostBack(\'ctl00$SiteContentPlaceHolder$FormView1$rblMailingAddrSame$1\',\'\')', 0);
}
document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_HOME_TEL').value = wx_data.p3_08;
setDirty();
if (wx_data.p3_09 == "") {
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_cbxAPP_MOBILE_TEL_NA').checked = true;
	setDirty();
	enableTbx('ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_MOBILE_TEL','ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_MOBILE_TEL_NA');
} else {
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_MOBILE_TEL').value = wx_data.p3_09;
	setDirty();
}
if (wx_data.p3_10 == "") {
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_cbxAPP_BUS_TEL_NA').checked = true;
	setDirty();
	enableTbx('ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_BUS_TEL','ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_BUS_TEL_NA');
} else {
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_BUS_TEL').value = wx_data.p3_10;
	setDirty();
}
document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_EMAIL_ADDR').value = wx_data.p3_11;
setDirty();
document.getElementById('ctl00_SiteContentPlaceHolder_UpdateButton3').click();

