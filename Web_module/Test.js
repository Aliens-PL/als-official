var fs = require('fs');


// for the moment only one file css and js 
const generate_document_header = (title,css_file,js_script)=>{
    return `<head>
                <meta charset="utf-8">
                <title>${title}</title>
                <link rel="stylesheet" href="${css_file}.css">
                <script src="${js_script}"></script>
            </head>`
}

const generate_content_display = (elements,className)=>{

        return (`<div class='${className}'>${return_items_to_render(elements)}</div>`)
}

const generate_paragraphe = (content,className)=>{
    //let paragraphe = new Paragraphe('test','test')
        return (`<p class='${className}'>${content}</p>`)
}

const generate_headline = (variant,className,headline_text,isBold)=>{
        return (`<h${variant} class='${className}'>${isBold?'<b>'+headline_text+'</b>':headline_text}</h${variant}>`)
}

const generate_default_container_ALS = (page_title,style,js,elements)=>{
    return (`<html>${generate_document_header(page_title,style,js)}<body><div class='container'>${return_items_to_render(elements)}</div></body></html>`)
}


const generate_image = (source,width,hiegth,className)=>{
    return (`<img  ${className?"class='"+className+"'":''} src='${source}' width='${width}px' hiegth='${hiegth}px' />`)
}

const generate_list_elements = (array)=>{
    let string ='';
    array.map(x=>{
       string =  string.concat(`<li>${x}</li>`)
       //tab.push(`<li>${x}</li>`)
    })
return string
}

const generate_list= (options,className)=>{
    return (`<ul ${className? "class='"+className+"'":''}>
                ${generate_list_elements(options)}
                
            </ul>
            `)
}



const return_items_to_render = (array)=>{
    let to_render ='';
    array.map(x=>{
        to_render =  to_render.concat(x)
    })
return to_render

}
 const p = generate_paragraphe('try','try');
 const dropdown = generate_list(['hello','ALS','111']);
 const img = generate_image('https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRtuJsCJezdhm0DRmP3cDTVUDZdrKn_uzS5IrMQeT-3VlK52LJT',100,100);
const headline = generate_headline(3,'test','hello');

const div_1 = generate_content_display([p,dropdown],'div_1_style');
const div_2 = generate_content_display([img,headline],'div_2_style')
 const dipslay = generate_default_container_ALS('mah_test','style','js',[div_1,div_2])
 fs.writeFile('./myPage.html',dipslay,(error) => { 

    console.log('error',error)
 })