import fool
"""
对数据进行预处理，生成ner对象，用ner来制作数据集
"""

raw_html = """
<div class="view-content">
      <div class="item-list">    <ol>          <li class="views-row views-row-1 views-row-odd views-row-first">  
  <div class="views-field views-field-title">        <span class="field-content"><a href="https://waimao.mingluji.com/node/114283?mip">深圳市顺意 进出口有限公司</a></span>  </div></li>
          <li class="views-row views-row-2 views-row-even">  
  <div class="views-field views-field-title">        <span class="field-content"><a href="https://waimao.mingluji.com/node/114284?mip">汕头市大树玩具 进出口有限公司</a></span>  </div></li>
          <li class="views-row views-row-3 views-row-odd">  
  <div class="views-field views-field-title">        <span class="field-content"><a href="https://waimao.mingluji.com/node/114285?mip">广州保税务区菱威智 国际贸易有限公司</a></span>  </div></li>
          <li class="views-row views-row-4 views-row-even">  
  <div class="views-field views-field-title">        <span class="field-content"><a href="https://waimao.mingluji.com/node/114286?mip">安徽远鹏 国际贸易有限公司</a></span>  </div></li>
          <li class="views-row views-row-5 views-row-odd">  
  <div class="views-field views-field-title">        <span class="field-content"><a href="https://waimao.mingluji.com/node/114287?mip">天津明川 国际贸易有限公司</a></span>  </div></li>
          <li class="views-row views-row-6 views-row-even">  
  <div class="views-field views-field-title">        <span class="field-content"><a href="https://waimao.mingluji.com/node/114288?mip">捷可星 国际贸易(上海)有限公司深圳分公司</a></span>  </div></li>
          <li class="views-row views-row-7 views-row-odd">  
  <div class="views-field views-field-title">        <span class="field-content"><a href="https://waimao.mingluji.com/node/114289?mip">深圳市长安 国际贸易有限公司</a></span>  </div></li>
          <li class="views-row views-row-8 views-row-even">  
  <div class="views-field views-field-title">        <span class="field-content"><a href="https://waimao.mingluji.com/node/114290?mip">深圳市家惠 国际贸易有限公司</a></span>  </div></li>
          <li class="views-row views-row-9 views-row-odd">  
  <div class="views-field views-field-title">        <span class="field-content"><a href="https://waimao.mingluji.com/node/114291?mip">北京安泰京钢 国际贸易有限公司</a></span>  </div></li>
          <li class="views-row views-row-10 views-row-even">  
  <div class="views-field views-field-title">        <span class="field-content"><a href="https://waimao.mingluji.com/node/114292?mip">中港海通 国际贸易(北京)有限公司</a></span>  </div></li>
          <li class="views-row views-row-11 views-row-odd">  
  <div class="views-field views-field-title">        <span class="field-content"><a href="https://waimao.mingluji.com/node/114293?mip">香港天龙 国际贸易有限公司</a></span>  </div></li>
          <li class="views-row views-row-12 views-row-even">  
  <div class="views-field views-field-title">        <span class="field-content"><a href="https://waimao.mingluji.com/node/114294?mip">千姿恋 国际贸易(北京)有限公司</a></span>  </div></li>
          <li class="views-row views-row-13 views-row-odd">  
  <div class="views-field views-field-title">        <span class="field-content"><a href="https://waimao.mingluji.com/node/114295?mip">千姿恋 国际贸易有限公司</a></span>  </div></li>
          <li class="views-row views-row-14 views-row-even">  
  <div class="views-field views-field-title">        <span class="field-content"><a href="https://waimao.mingluji.com/node/114296?mip">北京鸿玛视界 国际贸易有限公司</a></span>  </div></li>
          <li class="views-row views-row-15 views-row-odd views-row-last">  
  <div class="views-field views-field-title">        <span class="field-content"><a href="https://waimao.mingluji.com/node/114297?mip">深圳市南天辉 进出口有限公司</a></span>  </div></li>
      </ol></div>    </div>
  
      <div class="item-list"><ul class="pager"><li class="pager-previous first"><a href="https://waimao.mingluji.com/list?mip=&amp;page=100?mip">‹‹</a></li>
<li class="pager-current">第 102 页</li>
<li class="pager-next last"><a href="https://waimao.mingluji.com/list?mip=&amp;page=102?mip">››</a></li>
</ul></div>  
"""
_, ner = fool.analysis(text=raw_html)
print(ner)
