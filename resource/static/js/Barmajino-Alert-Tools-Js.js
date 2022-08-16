function destroy_alert(btn_clinked){
    let alert_div_ = btn_clinked.parentNode.parentNode.parentNode.parentNode;
    let main_div_ = btn_clinked.parentNode.parentNode.parentNode.parentNode.parentNode;
    main_div_.removeChild(alert_div_);
}

function alerts_testing() {
    let list_ = [
    ["bg-primary","text-white"],
    ["bg-secondary","text-white"],
   ["bg-success","text-white"],
    ["bg-danger","text-white"],
    ["bg-warning","text-white"],
    ["bg-info","text-white"],
    ["bg-dark","text-white"]
    ]
    for (var i = 0; i <= list_.length; i++){
        alert(list_[i][0], list_[i][1],list_[i][0], list_[i][1]);
    }
}
function alerting(bg_class, text_color_class, title, message){
    
    //create card main div 
    
    let card = document.createElement("div");
    card.setAttribute("class", "card textwhite " + bg_class + " " + text_color_class + "  shadow d-xl-flex ");
    card.setAttribute("style", "transform: perspective(0px);width: 250px;height: 80px; margin-bottom:8px;");
    card.setAttribute("data-aos", "fade-right");
    card.setAttribute("data-aos-duration", "400");
    card.setAttribute("data-aos-delay", "350");

    ////////////////////////////////////////////////////////////////////////////////////////////

    //create card-body main div
    let card_body = document.createElement("div");
    card_body.setAttribute("class", "card-body");

    card.appendChild(card_body);
    ////////////////////////////////////////////////////////////////////////////////////////////

    //create card-body-row  div
    let card_body_row = document.createElement("div");
    card_body_row.setAttribute("class", "row d-xl-flex align-items-xl-center");

    card_body.appendChild(card_body_row);
    ////////////////////////////////////////////////////////////////////////////////////////////

    //create card-body-row-col-1  div
    let card_body_row_col_1 = document.createElement("div");
    card_body_row_col_1.setAttribute("class", "col-md-6 col-xl-9");

    card_body_row.appendChild(card_body_row_col_1);
    ////////////////////////////////////////////////////////////////////////////////////////////

    //create card-body-row-col-1-p-1  p
    let card_body_row_col_1_p_1 = document.createElement("p");
    card_body_row_col_1_p_1.setAttribute("class", "m-0");
    card_body_row_col_1_p_1.innerText = title;

    card_body_row_col_1.appendChild(card_body_row_col_1_p_1);
    ////////////////////////////////////////////////////////////////////////////////////////////

    //create card-body-row-col-1-p-2  p
    let card_body_row_col_1_p_2 = document.createElement("p");
    card_body_row_col_1_p_2.setAttribute("class", "text-white-50 small m-0");
    card_body_row_col_1_p_2.innerText = message;

    card_body_row_col_1.appendChild(card_body_row_col_1_p_2);
    ////////////////////////////////////////////////////////////////////////////////////////////

    //create card-body-row-col-2  div
    let card_body_row_col_2 = document.createElement("div");
    card_body_row_col_2.setAttribute("class", "col-md-6 col-xl-3");

    card_body_row.appendChild(card_body_row_col_2);
    ////////////////////////////////////////////////////////////////////////////////////////////

    //create card-body-row-col-2-close-btn  button   <button class="btn link-light" type="button" data-bs-dismiss="alert" aria-label="Close" onclick="destroy_alert(this)">X</button>
    let card_body_row_col_2_close_btn = document.createElement("button");
    card_body_row_col_2_close_btn.setAttribute("class", "btn link-light");
    card_body_row_col_2_close_btn.setAttribute("type", "button");
    card_body_row_col_2_close_btn.setAttribute("data-bs-dismiss", "alert");
    card_body_row_col_2_close_btn.setAttribute("aria-label", "Close");
    card_body_row_col_2_close_btn.setAttribute("onclick", "destroy_alert(this)");
    card_body_row_col_2_close_btn.innerText = "X";

    card_body_row_col_2.appendChild(card_body_row_col_2_close_btn);
    ////////////////////////////////////////////////////////////////////////////////////////////





    let alerts = document.getElementById("alerts");
    alerts.appendChild(card);
}

function confirm(bg_class = "bg-info", text_color_class = "text-white", title = "Hi I'm Barmajino", message = "Bootstrap's Scrollspy allows you to automatically update nav targets based on scroll position. Scrollspy allows you to highlight the current position in a menu, based on the user's scroll position. As the user scrolls down the page, the applicable menu item is highlighted, based one where the scroll position is."){
    
    //create card main div 
    
    let card = document.createElement("div");
    card.setAttribute("class", "card textwhite " + bg_class + " " + text_color_class + "  shadow d-xl-flex ");
    card.setAttribute("style", "transform: perspective(0px);width: 260px; margin-bottom:8px; ");
    card.setAttribute("data-aos", "fade-right");
    card.setAttribute("data-aos-duration", "400");
    card.setAttribute("data-aos-delay", "350");
    card.setAttribute("scrolle", "True");

    ////////////////////////////////////////////////////////////////////////////////////////////

    //create card-body main div
    let card_body = document.createElement("div");
    card_body.setAttribute("class", "card-body");
    

    card.appendChild(card_body);
    ////////////////////////////////////////////////////////////////////////////////////////////

    //create card-body-row-1  div
    let card_body_row_1 = document.createElement("div");
    card_body_row_1.setAttribute("class", "row d-xl-flex align-items-xl-center");

    card_body.appendChild(card_body_row_1);
    ////////////////////////////////////////////////////////////////////////////////////////////

    //create card-body-row-3  div
    let card_body_row_3 = document.createElement("div");
    card_body_row_3.setAttribute("class", "row d-xl-flex align-items-xl-center");

    card_body.appendChild(card_body_row_3);
    ////////////////////////////////////////////////////////////////////////////////////////////

    //create card-body-row-1-col-1  div
    let card_body_row_1_col_1 = document.createElement("div");
    card_body_row_1_col_1.setAttribute("class", "col-md-6 col-xl-9");

    card_body_row_1.appendChild(card_body_row_1_col_1);
    ////////////////////////////////////////////////////////////////////////////////////////////

    //create card-body-row-1-col-1  div
    let card_body_row_3_col_1 = document.createElement("div");
    card_body_row_3_col_1.setAttribute("class", "col-12 col-sm-12 col-md-12 col-lg-12 col-xl-12 col-xxl-12 offset-0 offset-sm-0 offset-md-0 offset-lg-0 offset-xl-0 offset-xxl-0");

    card_body_row_3.appendChild(card_body_row_3_col_1);
    ////////////////////////////////////////////////////////////////////////////////////////////

    //create card-body-row-1-col-1-p-1  p
    let card_body_row_1_col_1_p_1 = document.createElement("p");
    card_body_row_1_col_1_p_1.setAttribute("class", "m-0");
    card_body_row_1_col_1_p_1.innerText = title;

    card_body_row_1_col_1.appendChild(card_body_row_1_col_1_p_1);
    ////////////////////////////////////////////////////////////////////////////////////////////
    

    //create card-body-row-3-col-1-p-2  p
    let card_body_row_3_col_1_p_2 = document.createElement("p");
    card_body_row_3_col_1_p_2.setAttribute("class", "text-white-50 small m-0");
    card_body_row_3_col_1_p_2.setAttribute("style", "overflow-x: hidden;overflow-y: auto; max-height: 60px;")
    card_body_row_3_col_1_p_2.innerText = message;

    card_body_row_3_col_1.appendChild(card_body_row_3_col_1_p_2);
    ////////////////////////////////////////////////////////////////////////////////////////////

    //create card-body-row-1-col-2  div
    let card_body_row_1_col_2 = document.createElement("div");
    card_body_row_1_col_2.setAttribute("class", "col-md-6 col-xl-3");

    card_body_row_1.appendChild(card_body_row_1_col_2);
    ////////////////////////////////////////////////////////////////////////////////////////////

    //create card-body-row-1-col-2-close-btn  button   
    let card_body_row_1_col_2_close_btn = document.createElement("button");
    card_body_row_1_col_2_close_btn.setAttribute("class", "btn link-light");
    card_body_row_1_col_2_close_btn.setAttribute("type", "button");
    card_body_row_1_col_2_close_btn.setAttribute("data-bs-dismiss", "alert");
    card_body_row_1_col_2_close_btn.setAttribute("aria-label", "Close");
    card_body_row_1_col_2_close_btn.setAttribute("onclick", "destroy_alert(this)");
    card_body_row_1_col_2_close_btn.innerText = "X";

    card_body_row_1_col_2.appendChild(card_body_row_1_col_2_close_btn);
    ////////////////////////////////////////////////////////////////////////////////////////////

/*<div class="row d-xl-flex align-items-xl-center">
    <div class=""><button  type="button"   onclick="destroy_alert(this)">Yes</button></div>
    <div class="col-3 col-sm-3 col-md-3 col-xl-3"><button class="btn btn-danger link-light" type="button" data-bs-dismiss="alert" aria-label="Close" onclick="destroy_alert(this)">No</button></div>
</div>*/

    //create card-body-row-2  div
    let card_body_row_2 = document.createElement("div");
    card_body_row_2.setAttribute("class", "row d-xl-flex align-items-xl-center");
    card_body_row_2.setAttribute("style", "margin-top:10px;");

    card_body.appendChild(card_body_row_2);
    ////////////////////////////////////////////////////////////////////////////////////////////

    //create card-body-row-2-col-1  div
    let card_body_row_2_col_1 = document.createElement("div");
    card_body_row_2_col_1.setAttribute("class", "col-4 col-sm-4 col-md-4 col-lg-4 col-xl-4 col-xxl-4 offset-2 offset-sm-2 offset-md-2 offset-lg-2 offset-xl-2 offset-xxl-2");

    card_body_row_2.appendChild(card_body_row_2_col_1);
    ////////////////////////////////////////////////////////////////////////////////////////////

    //create card-body-row-2-col-2-btn  button   
    let card_body_row_2_col_1_btn = document.createElement("button");
    card_body_row_2_col_1_btn.setAttribute("class", "btn btn-success link-light");
    card_body_row_2_col_1_btn.setAttribute("type", "button");
    card_body_row_2_col_1_btn.setAttribute("aria-label", "yes");
    card_body_row_2_col_1_btn.setAttribute("id", "yes_btn");
    card_body_row_2_col_1_btn.innerText = "Yes";

    card_body_row_2_col_1.appendChild(card_body_row_2_col_1_btn);
    ////////////////////////////////////////////////////////////////////////////////////////////

    //create card-body-row-2-col-1  div
    let card_body_row_2_col_2 = document.createElement("div");
    card_body_row_2_col_2.setAttribute("class", "col-3 col-sm-3 col-md-3 col-xl-3");

    card_body_row_2.appendChild(card_body_row_2_col_2);
    ////////////////////////////////////////////////////////////////////////////////////////////

    //create card-body-row-2-col-2-btn  button   
    let card_body_row_2_col_2_btn = document.createElement("button");
    card_body_row_2_col_2_btn.setAttribute("class", "btn btn-danger link-light");
    card_body_row_2_col_2_btn.setAttribute("type", "button");
    card_body_row_2_col_2_btn.setAttribute("aria-label", "yes");
    card_body_row_2_col_2_btn.setAttribute("id", "no_btn");
    card_body_row_2_col_2_btn.innerText = "No";

    card_body_row_2_col_2.appendChild(card_body_row_2_col_2_btn);
    ////////////////////////////////////////////////////////////////////////////////////////////

    let alerts = document.getElementById("alerts");
    alerts.appendChild(card);
}