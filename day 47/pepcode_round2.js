
const puppeteer=require('puppeteer');

async function scrapeProduct(url){

  const browser=await puppeteer.launch();
  const page=await browser.newPage();
  await page.goto(url);
  const [el]=await page.$x('/html/body/div[3]/div[3]/div[5]/div[1]/p[5] ');
  const src= await el.getProperty('textContent');
  const History=await src.jsonValue();

  const [el1]=await page.$x('//*[@id="mw-content-text"]/div[1]/p[6]');
  const src1= await el1.getProperty('textContent');
  const History2=await src1.jsonValue();

  const [el2]=await page.$x('//*[@id="mw-content-text"]/div[1]/p[7]');
  const src2= await el2.getProperty('textContent');
  const History3=await src2.jsonValue();

  const [el3]=await page.$x('//*[@id="mw-content-text"]/div[1]/p[8]');
  const src3= await el3.getProperty('textContent');
  const TopographicContent=await src3.jsonValue();

  const [el4]=await page.$x('//*[@id="mw-content-text"]/div[1]/p[9]');
  const src4= await el4.getProperty('textContent');
  const TopographicContent1=await src4.jsonValue();

  const [el5]=await page.$x('//*[@id="mw-content-text"]/div[1]/p[10]');
  const src5= await el5.getProperty('textContent');
  const TopographicContent2=await src5.jsonValue();

  const [el6]=await page.$x('//*[@id="mw-content-text"]/div[1]/p[10]');
  const src6= await el6.getProperty('textContent');
  const TopographicContent3=await src6.jsonValue();

  const [el7]=await page.$x('//*[@id="mw-content-text"]/div[1]/p[11]');
  const src7= await el7.getProperty('textContent');
  const TopographicContent4=await src7.jsonValue();

  const [el8]=await page.$x('//*[@id="mw-content-text"]/div[1]/p[12]');
  const src8= await el8.getProperty('textContent');
  const useInWritingSection=await src8.jsonValue();

  const [el9]=await page.$x('//*[@id="mw-content-text"]/div[1]/ul[1]');
  const src9= await el9.getProperty('textContent');
  const useInWritingSection1=await src9.jsonValue();

  const [el11]=await page.$x('//*[@id="mw-content-text"]/div[1]/p[13]');
  const src11= await el11.getProperty('textContent');
  const useInWritingSection2=await src11.jsonValue();

  const [el12]=await page.$x('//*[@id="mw-content-text"]/div[1]/p[14]');
  const src12= await el12.getProperty('textContent');
  const useInWritingSection3=await src12.jsonValue();

  const [el13]=await page.$x('//*[@id="mw-content-text"]/div[1]/p[15]');
  const src13= await el13.getProperty('textContent');
  const otherLanguages=await src13.jsonValue();

  const [el14]=await page.$x('//*[@id="mw-content-text"]/div[1]/ul[2]');
  const src14= await el14.getProperty('textContent');
  const othersystem=await src14.jsonValue();






  console.log({History,History2,History3,TopographicContent,TopographicContent1,TopographicContent2,TopographicContent4,useInWritingSection,useInWritingSection1,useInWritingSection2,useInWritingSection3,otherLanguages,othersystem});
  browser.close();
}
scrapeProduct('https://en.wikipedia.org/wiki/A');