var fs = require('fs');


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

const generate_default_container_ALS = (elements)=>{
    return (`<div class='container'>${elements}</div>`)
}


const generate_image = (source,width,hiegth,className)=>{
    return (`<img  ${className?"class='"+className+"'":null} src='${source}' width='${width}px' hiegth='${hiegth}px' />`)
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
// const img = generate_image('https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRtuJsCJezdhm0DRmP3cDTVUDZdrKn_uzS5IrMQeT-3VlK52LJT',100,100);
//const headline = generate_headline(3,'test','hello');
 const dipslay = generate_content_display([p,dropdown],'container')
 fs.writeFile('./myPage.html',dipslay,(error) => { 

    console.log('error',error)
 })