wx_data = eval('('+wx_data+')');
document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_SURNAME').value = wx_data.p1_01;
setDirty();
document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_GIVEN_NAME').value = wx_data.p1_02;
setDirty();
document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_FULL_NAME_NATIVE').value = wx_data.p1_03;
setDirty();
if (wx_data.p1_04 == 1) {
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_rblOtherNames_0').checked = true;
} else {
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_rblOtherNames_1').checked = true;
}
setDirty();
setTimeout('__doPostBack(\'ctl00$SiteContentPlaceHolder$FormView1$rblOtherNames$1\',\'\')', 0);
if (wx_data.p1_04 == 1) {
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_DListAlias_ctl00_tbxSURNAME').value = wx_data.p1_04_01;
	setDirty();
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_DListAlias_ctl00_tbxGIVEN_NAME').value = wx_data.p1_04_02;
	setDirty();
}
if (wx_data.p1_05 == 1) {
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_rblTelecodeQuestion_0').checked = true;
} else {
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_rblTelecodeQuestion_1').checked = true;
}
setDirty();
setTimeout('__doPostBack(\'ctl00$SiteContentPlaceHolder$FormView1$rblTelecodeQuestion$1\',\'\')', 0);
if (wx_data.p1_05 == 1) {
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_TelecodeSURNAME').value = wx_data.p1_05_01;
	setDirty();
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_TelecodeGIVEN_NAME').value = wx_data.p1_05_02;
	setDirty();
}
if (wx_data.p1_06 == 1) {
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_rblAPP_GENDER_0').checked = true;
} else {
	document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_rblAPP_GENDER_1').checked = true;
}
setDirty();
document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_ddlAPP_MARITAL_STATUS').value = wx_data.p1_07;
setDirty();
setTimeout('__doPostBack(\'ctl00$SiteContentPlaceHolder$FormView1$ddlAPP_MARITAL_STATUS\',\'\')', 0)
document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_ddlDOBDay').value = wx_data.p1_08;
setDirty();
document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_ddlDOBMonth').value = wx_data.p1_09;
setDirty();
document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_tbxDOBYear').value = wx_data.p1_10;
setDirty();
document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_POB_CITY').value = wx_data.p1_11;
setDirty();
document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_tbxAPP_POB_ST_PROVINCE').value = wx_data.p1_12;
setDirty();
document.getElementById('ctl00_SiteContentPlaceHolder_FormView1_ddlAPP_POB_CNTRY').value = wx_data.p1_13;
setDirty();
document.getElementById('ctl00_SiteContentPlaceHolder_UpdateButton3').click();
