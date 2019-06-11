//yangtbpres = ''
//var yDatatablespres = function(yurl, ydiv, ytable, yy=400, yorder=false) {
//    console.log("START yDatatablespres : " + yurl + " , " + ydiv + " , " + ytable)
//    $.ajax({
//        "url": '/' + yurl,  //"url": '/Ajob',
//        "dataType": "json",
//        "success": function(json) {
////            yfdt(json, ydiv, ytable, yy, yorder);
//            if (json.columns.length > 0) {
//                var tableHeaders = "";
//
//                $.each(json.columns, function(i, val){
//                    tableHeaders += "<th>" + val + "</th>";
//                });
//                $('#' + ydiv).empty();
//                $('#' + ydiv).append('<table id="' + ytable + '" class="table table-bordered display dtytable" cellspacing="0" width="100%"><thead><tr class="success">' + tableHeaders + '</tr></thead></table>');
//
//                yangtbpres = $('#' + ytable).removeAttr('width').DataTable({
//                    "destroy": true,
//                    "data": json.data,
//                    "scrollY": yy,
//                    "paging" : false,
//                    "AutoWidth": false,
//                    "FixedHeader": true,
//                    "ordering": yorder,
//                    "columnDefs": [
//                        { "targets": [0],   //30
//                           "width": "9%"
//                        },
//                        {
//                            "targets": [ -1 ],
//                            "data": null,
//                            "defaultContent": '<button type="button" class="btn btn-info btn-xs" data-toggle="modal" data-target="#yModalinputpres">수정</button>'
//                        }
//                    ]
//                });
//
//            }else {
//                console.log("Yang Error json.length == 0")
//            }
//        }
//    });
//}
var yDatatablesmodalpres = function(ap0,ap1,ap2,ap3,ap4,   ap5,ap6,ap7,ap8,ap9) {
    console.log("START yDatatablesmodalpres 0~8 APRESMODAL : " + ap0 + " , " + ap1 + " , " + ap2 + " , " + ap3)
    $.ajax({
        "url": 'APRESMODAL',   //'/' + yurl,  //"url": '/Ajob',
        "dataType": "json",
        "data": {
            'ys0' : ap0,
            'ys1' : ap1,
            'ys2' : ap2,
            'ys3' : ap3,
            'ys4' : ap4,

            'ys5' : ap5,
            'ys6' : ap6,
            'ys7' : ap7,
            'ys8' : ap8,
            'ys9' : ap9
        },
        "success": function(json) {
            yfdtbtn(json, "ydiv0", "ytable0", "yModalinputpres", 700);
        }
    });
}
//
//
//var yDatatablespres = function(yurl, ydiv, ytable, yy=400, yorder=false) {
//    console.log("START yDatatablespres yfdtbtn : " + yurl + " , " + ydiv + " , " + ytable)
//    $.ajax({
//        "url": '/' + yurl,
//        "dataType": "json",
//        "success": function(json) {
//            yfdtbtn(json, ydiv, ytable, yy, yorder);
//        }
//    });
//}
/////////////////////////////////////////////////////////////////////////////////////////////////////////
// DataTable yfdt
/////////////////////////////////////////////////////////////////////////////////////////////////////////
yangtb = ''
var yfdt = function(json, ydivmon, ytablemon, yy=730, yorder=false) {
    console.log('Start yfdt !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!');
    if (json.columns.length > 0) {
        var tableHeaders = "";

        $.each(json.columns, function(i, val){
            tableHeaders += "<th>" + val + "</th>";
        });
        $('#' + ydivmon).empty();
        $('#' + ydivmon).append('<table id="' + ytablemon + '" class="table table-bordered display dtytable" cellspacing="0" width="100%"><thead><tr class="success">' + tableHeaders + '</tr></thead></table>');

        yangtb = $('#' + ytablemon).removeAttr('width').DataTable({
            "destroy": true,
            "data": json.data,
//            "dom": 'Bfrtip',
//            "buttons": [
//                'copy', 'csv', 'excel', 'pdf'
//            ],
            "scrollY": yy,
            "paging" : false,
            "AutoWidth": false,
            "FixedHeader": true,
            "ordering": yorder,
            "bInfo" : false,
            "columnDefs": [
                { "targets": [0],   //30
                   "width": "9%"
                }
            ]
        });

    }else {
        console.log("Yang Error json.length == 0")
    }
}

yangtbbtnpres = ''
var yfdtbtn = function(json, ydivmon, ytablemon, yModalname, yy=730, yorder=false) {
    console.log('Start yfdtbtn !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!');
    if (json.columns.length > 0) {
        var tableHeaders = "";

        $.each(json.columns, function(i, val){
            tableHeaders += "<th>" + val + "</th>";
        });
        $('#' + ydivmon).empty();
        $('#' + ydivmon).append('<table id="' + ytablemon + '" class="table table-bordered display dtytable" cellspacing="0" width="100%"><thead><tr class="success">' + tableHeaders + '</tr></thead></table>');

        var yangtbbtn = $('#' + ytablemon).removeAttr('width').DataTable({
            "destroy": true,
            "data": json.data,
            "scrollY": yy,
            "paging" : false,
            "AutoWidth": false,
            "FixedHeader": true,
            "ordering": yorder,
            "columnDefs": [
                { "targets": [0],   //30
                   "width": "9%"
                },
                {
                    "targets": [ -1 ],
                    "data": null,
                    "defaultContent": '<button type="button" class="btn btn-info btn-xs" data-toggle="modal" data-target="#' + yModalname + '">수정</button>'
                }
            ]
        });

        yangtbbtnpres = yangtbbtn;

    }else {
        console.log("Yang Error json.length == 0")
    }
}


var yDatatables = function(yurl, ydiv, ytable, yy=400, yorder=false) {
    console.log("START yDatatables yfdt : " + yurl + " , " + ydiv + " , " + ytable)
    $.ajax({
        "url": '/' + yurl,  //"url": '/Ajob',
        "dataType": "json",
        "success": function(json) {
            yfdt(json, ydiv, ytable, yy, yorder);
        }
    });
}
var yDatatablesbtn = function(yurl, ydiv, ytable, yy=400, yorder=false) {
    console.log("START yDatatablesbtn yfdtbtn : " + yurl + " , " + ydiv + " , " + ytable)
    $.ajax({
        "url": '/' + yurl,  //"url": '/Ajob',
        "dataType": "json",
        "success": function(json) {
            yfdtbtn(json, ydiv, ytable, yy, yorder);
        }
    });
}
var yDatatablesmodal = function(yurl, ydiv, ytable, yModalname, yy=400, yorder=false) {
    console.log("START yDatatablesbtn yfdtbtn : " + yurl + " , " + ydiv + " , " + ytable)
    $.ajax({
        "url": '/' + yurl,  //"url": '/Ajob',
        "dataType": "json",
        "success": function(json) {
            yfdtbtn(json, ydiv, ytable, yModalname, yy, yorder);
        }
    });
}
var yDatatablesMan = function(yurl, ydiv, ytable, apara1, yy=650, yorder=false) {
    console.log("START yDatatablesMan yfdt : " + yurl + " , " + ydiv  + " , " + ytable + " , " + apara1)
    $.ajax({
        "url": '/' + yurl,  //"url": '/Ajob',
        "dataType": "json",
        "data": {
            'ys1' : apara1
        },
        "success": function(json) {
            yfdt(json, ydiv, ytable, yy, yorder);
        }
    });
}




ydtvocold = ''
//////////////  Dom /////////////////////////////////////////////////////////////////////////////////////////////
//////////////  Dom /////////////////////////////////////////////////////////////////////////////////////////////
$(document).ready(function() {
    $("#tabs").tabs({
        activate: function( event, ui ){
            var selectedTab = $("#tabs").tabs('option', 'active'); // 선택된 tab의 index value
            if(selectedTab == 0){
                $("#tabs").tabs({ active: 0 })
                yDatatablespres('APRES', "ydiv0", "ytable0", 700);
            } else if(selectedTab == 1){
                $("#tabs").tabs({ active: 1 })
                yDatatablesbtn('ACUST', "ydiv1", "ytable1", 700);
            } else if(selectedTab == 2){
                $("#tabs").tabs({ active: 2 })
                yDatatablesbtn('APEOP', "ydiv2", "ytable2", 700);
            }  else if(selectedTab == 3){
                $("#tabs").tabs({ active: 3 })
                yDatatablesbtn('AREGI', "ydiv3", "ytable3", 700);
            }  else if(selectedTab == 4){
                $("#tabs").tabs({ active: 4 })
                yDatatablesbtn('AWORK', "ydiv4", "ytable4", 700);
            }  else if(selectedTab == 5){
                $("#tabs").tabs({ active: 5 })
                yDatatables('AGOOD', "ydiv5", "ytable5", 200);
            }  else if(selectedTab == 6){
                $("#tabs").tabs({ active: 6 })
                yDatatables('AMORE', "ydiv6", "ytable6", 700);
            }  else if(selectedTab == 7){
                $("#tabs").tabs({ active: 7 })
                yDatatables('APAY', "ydiv7", "ytable7", 700, true);
            }  else if(selectedTab == 8){
                $("#tabs").tabs({ active: 8 })
                yDatatables('ASCHA', "ydiv81", "ytable81", 200);
                yDatatables('ASCHB', "ydiv82", "ytable82", 200);
                yDatatables('ASCHC', "ydiv83", "ytable83", 200);
            }
        }
    });

    // datepicker ////////////////////////////////////////////////////////////
    $( "#datepickersch82" ).datepicker({
        dateFormat: 'yy-mm-dd',
        showOtherMonths: true,
        selectOtherMonths: true,
        showButtonPanel: true,
        //minDate: -31,
        //maxDate: "+0D"
    });
    
//////////////  최초시작 /////////////////////////////////////////////////////////////////////////////////////////////
    yDatatablesmodal('APRES', "ydiv0", "ytable0", "yModalinputpres", 700);

///////////////////////////////////////////////////////////////////////////////////////////////////////
// 1분마다
///////////////////////////////////////////////////////////////////////////////////////////////////////


//    window.setInterval(function(){
//        console.log('Sched Start1 !!!');
//        $.ajax({
//            url: '/AServer',   //'static/testdata/arrays_short2.txt',  //'/AjaxTable1_4',
//            dataType: "json", //ydtstr4
//            success: function(json) {
//                console.log(json);
//    //            var yvocdtnew = json;
//    //            $("#btn_TopR1").val('UPDATE시각:' + yvocdtnew);
//    //            ydtvocold = yvocdtnew;
//            }
//        });
//        yDatatablestop('AjaxTable0', "ydiv0", "ytable0", 150);
//        yDatatables('AjaxTable1', "ydiv1", "ytable1", 300);
//        yDatatables('AjaxTable12', "ydiv12", "ytable12", 200);
//    }, 120*1000);  //interval 120초


//////////////  Event /////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////
// Event
/////////////////////////////////////////////////////////////////////////////////////////////////////////
    $('ytable').on( 'click', 'tbody tr', function () {
        if ( $(this).hasClass('selected') ) {
            $(this).removeClass('selected');
        }
        else {
            $(this).addClass('selected');
        }
    });

    $('#ydiv1').on('dblclick', 'tbody td', function() {
        var td_val = $(this).text();
        var td_icol = $(this).index();
        var tbid = $(this).closest('table').attr('id');

        var td_first = $(this).siblings("td:first").text();

        console.log('dbclicked :' + td_val + ' , ' + td_icol.toString() + ' , ' + tbid  + ' , ' + td_first);
        if (td_icol == 0){
            if (td_val.length > 2) {
                $('#yModal').modal('show');
                setTimeout(function(){
                    yDatatablesMan('AjaxMan', 'ydivmodal', 'ytablemodal', td_val, 450);
                    // $("#ycomma").val(comma);
                }, 1000);
            }
        }
    });



    $('#btn_query').click(function(){
        var ymanqry = $( "#qry_filter" ).val();
        console.log("Clicked btn_query : " + ymanqry)
        if (ymanqry.length > 2) {
            yDatatablesMan('AjaxMan', 'ydiv9', 'ytable9', ymanqry, 650);
        }

    });



    $('#ydiv0').on( 'click', 'button', function () {
        console.log('ydiv0 button clicked !!!');
        // console.log(yangtbpres);
        var data = yangtbbtnpres.row( $(this).parents('tr') ).data();
        console.log(data);
        $("#yidpres").val(data[0]);
        $("#ydatepres").val(data[1]);
        $("#yweekpres").val(data[2]);
        $("#ytimepres").val(data[3]);
        $("#yname1pres").val(data[4]);
        $("#ycountpres").val(data[5]);
        $("#yname2pres").val(data[6]);
        $("input[name='yrahourpres'][value='" + data[7] + "']").prop("checked",true);
        $("#yetcpres").val(data[8]);


        $('#ysavepres').css("display", "none");

        if ($("#ysavemodpres").css("display") == "none"){
            $('#ysavemodpres').show()
        }

//        $('#ysavepres').css("display", "none");
//        $('#ysavemodpres').css("display", "block");
    });
    $('#btn_pres').click(function(){
        console.log('btn_pres clicked !!!');
        $("#yidpres").val("");
        $("#ydatepres").val("");
        $("#yweekpres").val("");
        $("#ytimepres").val("");
        $("#yname1pres").val("");
        $("#ycountpres").val("");
        $("#yname2pres").val("");
        $("input[name='yrahourpres'][value='1']").prop("checked",true);
        $("#yetcpres").val("");

        if ($("#ysavepres").css("display") == "none"){
            $('#ysavepres').show()
        }
        $('#ysavemodpres').css("display", "none");

    });
    $('#ysavemodpres').click(function(){
        var yidpres = $( "#yidpres" ).val();
        var ydatepres = $("#ydatepres").val();
        var yweekpres = $("#yweekpres").val();
        var ytimepres = $("#ytimepres").val();
        var yname1pres = $("#yname1pres").val();

        var ycountpres = $("#ycountpres").val();
        var yname2pres = $("#yname2pres").val();
        var yrahourpres = $("input[name='yrahourpres']:checked").val();
        var yetcpres = $("#yetcpres").val();

        console.log("Clicked ysavemodpres 1~ : " + yidpres + " , " + ydatepres + " , " + ytimepres + " , " + yname1pres)
        yDatatablesmodalpres('Modify', yidpres, ydatepres, yweekpres, ytimepres, yname1pres,          ycountpres, yname2pres, yrahourpres, yetcpres);
    });
    $('#ysavepres').click(function(){
        var yidpres = 'CreateID' //$( "#yidpres" ).val();
        var ydatepres = $("#ydatepres").val();
        var yweekpres = $("#yweekpres").val();
        var ytimepres = $("#ytimepres").val();
        var yname1pres = $("#yname1pres").val();

        var ycountpres = $("#ycountpres").val();
        var yname2pres = $("#yname2pres").val();
        var yrahourpres = $("input[name='yrahourpres']:checked").val();
        var yetcpres = $("#yetcpres").val();

        console.log("Clicked ysave 1~ : " + yidpres + " , " + ydatepres + " , " + ytimepres + " , " + yname1pres)
        yDatatablesmodalpres('Create', yidpres, ydatepres, yweekpres, ytimepres, yname1pres,          ycountpres, yname2pres, yrahourpres, yetcpres);
    });





} );





