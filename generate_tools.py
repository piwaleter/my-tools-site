#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
跨境电商计算器批量生成工具 —— 把 generate_tools.py 在终端跑一下就能生成100+个工具页面
使用方法：
  python generate_tools.py
"""

import os
import datetime

CURRENT_YEAR = "2026"

# ============================================================
#  平台配置数据：平台 × 国家 × 品类
# ============================================================

# 各国货币符号
CURRENCY = {
    "US": "$", "UK": chr(0xA3), "DE": chr(0x20AC), "FR": chr(0x20AC),
    "JP": chr(0xA5), "CA": "C$", "AU": "A$", "AE": "AED ",
    "IT": chr(0x20AC), "ES": chr(0x20AC), "SG": "S$", "ID": "Rp ",
    "TH": chr(0x0E3F), "VN": "₫", "MY": "RM ", "PH": chr(0x20B1),
    "MX": "Mex$", "BR": "R$", "AR": "ARS$", "CO": "COL$",
}

def ccy(code):
    return CURRENCY.get(code, "$")

# -----------------------------------------------------------
#  每个平台的国家品类矩阵
# -----------------------------------------------------------
PLATFORMS = [
    # ========== Amazon ==========
    {"id": "amazon", "name": "Amazon", "label": "Amazon", "color": "orange",
     "countries": ["US","UK","DE","FR","JP","CA","AU","AE"],
     "categories": ["Electronics","Clothing","Beauty","Home-Kitchen","Sports"],
     "fee_type": "amazon"},

    # ========== TikTok Shop ==========
    {"id": "tiktok", "name": "TikTok Shop", "label": "TikTok Shop", "color": "black",
     "countries": ["US","UK","ID","TH","VN","MY","PH","SG"],
     "categories": ["Beauty","Fashion","Electronics"],
     "fee_type": "tiktok"},

    # ========== Shopify ==========
    {"id": "shopify", "name": "Shopify", "label": "Shopify", "color": "emerald",
     "countries": ["US","UK","CA","AU","DE","FR"],
     "categories": ["Clothing","Home-Kitchen","Beauty"],
     "fee_type": "shopify"},

    # ========== Etsy ==========
    {"id": "etsy", "name": "Etsy", "label": "Etsy", "color": "amber",
     "countries": ["US","UK","DE","FR","CA","AU"],
     "categories": ["Handmade","Clothing","Home-Kitchen"],
     "fee_type": "etsy"},

    # ========== eBay ==========
    {"id": "ebay", "name": "eBay", "label": "eBay", "color": "blue",
     "countries": ["US","UK","DE","AU","FR","IT","CA"],
     "categories": ["Electronics","Clothing","Collectibles"],
     "fee_type": "ebay"},

    # ========== Walmart ==========
    {"id": "walmart", "name": "Walmart", "label": "Walmart", "color": "blue",
     "countries": ["US","CA"],
     "categories": ["Electronics","Home-Kitchen","Clothing"],
     "fee_type": "walmart"},

    # ========== Mercado Libre ==========
    {"id": "mercadolibre", "name": "Mercado Libre", "label": "Mercado Libre", "color": "yellow",
     "countries": ["MX","BR","AR","CO"],
     "categories": ["Electronics","Fashion","Home-Kitchen"],
     "fee_type": "mercadolibre"},
]

# -----------------------------------------------------------
#  品类显示名称
# -----------------------------------------------------------
CATEGORY_LABELS = {
    "Electronics": "Electronics", "Clothing": "Clothing / Fashion",
    "Beauty": "Beauty & Cosmetics", "Home-Kitchen": "Home & Kitchen",
    "Sports": "Sports & Outdoors", "Handmade": "Handmade & Crafts",
    "Collectibles": "Collectibles & Vintage", "Fashion": "Fashion",
    "Automotive": "Automotive Parts",
}
CATEGORY_LABELS_CN = {
    "Electronics": "电子产品", "Clothing": "服装", "Beauty": "美妆个护",
    "Home-Kitchen": "家居厨房", "Sports": "运动户外",
    "Handmade": "手工艺品", "Collectibles": "收藏品",
    "Fashion": "时尚", "Automotive": "汽车配件",
}

def cat_label(cat):
    return CATEGORY_LABELS.get(cat, cat)

def cat_label_cn(cat):
    return CATEGORY_LABELS_CN.get(cat, cat)

# ============================================================
#  HTML 生成器
# ============================================================

def build_amazon_html(p, c, cat):
    """Amazon 计算器"""
    symbol = ccy(p["countries"][c])
    country = p["countries"][c]
    plat_name = p["name"]
    # Some countries have different referral fee structures
    # Using standard tiered 8%/15% for most, 12-15% for clothing
    cat_slug = cat.lower()
    ref_rate = "0.08"
    ref_rate_high = "0.15"
    ref_threshold = "200"
    if cat == "Clothing":
        ref_rate = "0.12"
        ref_rate_high = "0.15"
        ref_threshold = "100"

    title = f"{plat_name} {country} {cat_label(cat)} Profit & ROI Calculator ({CURRENT_YEAR})"
    desc = f"Calculate your {plat_name} {country} {cat_label(cat)} FBA product profit, margin, and ROI. Up-to-date {CURRENT_YEAR} referral fees and fulfillment rates."
    keywords = f"{plat_name} {country} calculator, {cat_label(cat)} profit calculator, FBA fee {CURRENT_YEAR}, margin calculator"
    h1 = f"{plat_name} {country} FBA Profit Calculator"
    span_text = f"{cat_label_cn(cat)}"

    # Platform tag
    platform_tag = f"{plat_name} {country}"
    currency_symbol = symbol

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <meta name="keywords" content="{keywords}">
    <link rel="stylesheet" href="tailwind.css">
    <style>.blur-overlay{{backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)}}</style>
</head>
<body class="bg-gray-50 text-gray-800 font-sans antialiased">

<header class="bg-white border-b border-gray-200 sticky top-0 z-40 shadow-sm">
    <div class="max-w-5xl mx-auto px-4 py-4 flex justify-between items-center">
        <div class="flex items-center space-x-2">
            <span class="text-2xl">⚡</span>
            <span class="font-bold text-xl tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-yellow-500 to-orange-600">SellerTools Pro</span>
        </div>
        <div class="flex items-center space-x-4">
            <span class="text-xs text-green-600 bg-green-50 px-2.5 py-1 rounded-full font-medium">● {CURRENT_YEAR} Live Rates</span>
            <button onclick="showLicenseModal()" class="text-xs bg-gray-900 hover:bg-gray-800 text-white px-3 py-1.5 rounded-lg font-medium transition">Activate PRO</button>
        </div>
    </div>
</header>

<main class="max-w-5xl mx-auto px-4 py-10 grid grid-cols-1 md:grid-cols-3 gap-8">
    <section class="md:col-span-2 bg-white border border-gray-200 rounded-2xl p-6 shadow-sm">
        <h1 class="text-2xl font-bold text-gray-900 mb-6">{h1} <span class="text-orange-500 text-lg">({span_text})</span></h1>
        <div class="space-y-6">
            <div>
                <h2 class="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-3">1. Pricing & Costs</h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Selling Price ({currency_symbol})</label>
                        <input type="number" id="sellingPrice" value="49.99" class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none transition">
                    </div>
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Product Cost ({currency_symbol})</label>
                        <input type="number" id="productCost" value="12.50" class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none transition">
                    </div>
                </div>
            </div>
            <div>
                <h2 class="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-3">2. Logistics & Shipping</h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Shipping to FBA ({currency_symbol}/unit)</label>
                        <input type="number" id="shippingCost" value="3.20" class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none transition">
                    </div>
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-1">FBA Fulfillment Fee ({currency_symbol}/unit)</label>
                        <input type="number" id="fbaFee" value="5.40" class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none transition">
                    </div>
                </div>
            </div>
            <div>
                <h2 class="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-3">3. Marketing & Ads (Optional)</h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-1">PPC Cost per Unit ({currency_symbol})</label>
                        <input type="number" id="ppcCost" value="4.50" class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none transition">
                    </div>
                </div>
            </div>
            <button onclick="calculateProfit()" class="w-full bg-gradient-to-r from-yellow-500 to-orange-600 hover:from-yellow-600 hover:to-orange-700 text-white font-semibold py-3 px-4 rounded-xl shadow-md transition transform active:scale-95">Calculate ROI & Profit</button>
        </div>
    </section>

    <section class="bg-gray-900 text-white rounded-2xl p-6 shadow-xl flex flex-col justify-between relative overflow-hidden">
        <div>
            <h2 class="text-lg font-bold tracking-tight text-gray-300 mb-6">Financial Summary</h2>
            <div class="space-y-4">
                <div class="flex justify-between border-b border-gray-800 pb-2">
                    <span class="text-gray-400">Referral Fee</span>
                    <span id="referralFeeDisplay" class="font-medium">{currency_symbol}0.00</span>
                </div>
                <div class="flex justify-between border-b border-gray-800 pb-2">
                    <span class="text-gray-400">Total Expenses</span>
                    <span id="totalExpensesDisplay" class="font-medium">{currency_symbol}0.00</span>
                </div>
                <div class="flex justify-between pt-2">
                    <span class="text-gray-200 font-semibold text-lg">Net Profit</span>
                    <span id="netProfitDisplay" class="text-2xl font-bold text-green-400">{currency_symbol}0.00</span>
                </div>
                <div class="flex justify-between">
                    <span class="text-gray-400">Net Margin</span>
                    <span id="marginDisplay" class="font-medium text-green-400">0.00%</span>
                </div>
                <div class="flex justify-between">
                    <span class="text-gray-400">ROI</span>
                    <span id="roiDisplay" class="font-medium text-green-400">0.00%</span>
                </div>
            </div>
        </div>
        <div class="mt-8 pt-6 border-t border-gray-800">
            <button onclick="triggerPaywallAction()" class="w-full bg-yellow-500 hover:bg-yellow-400 text-gray-950 font-bold py-3 px-4 rounded-xl flex items-center justify-center space-x-2 transition shadow-lg">
                <span>📊</span>
                <span>Export Premium PDF Report</span>
            </button>
            <p class="text-center text-xs text-gray-500 mt-2">🔒 Pro feature. Requires activation key.</p>
        </div>
    </section>
</main>

<div id="paywallModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 bg-gray-950 bg-opacity-60 blur-overlay">
    <div class="bg-white rounded-2xl max-w-md w-full p-6 shadow-2xl relative border border-gray-100 text-gray-800">
        <button onclick="closePaywallModal()" class="absolute top-4 right-4 text-gray-400 hover:text-gray-600 text-xl" style="background:none;border:none;cursor:pointer;">&times;</button>
        <div class="text-center mb-6">
            <span class="text-4xl">💎</span>
            <h3 class="text-xl font-bold text-gray-900 mt-2">Unlock Premium Exporter</h3>
            <p class="text-sm text-gray-500 mt-1">Export professional PDF profit reports for supplier negotiations.</p>
        </div>
        <div class="bg-gray-50 rounded-xl p-4 mb-6 border border-gray-200">
            <div class="flex justify-between items-center">
                <div>
                    <p class="font-semibold text-gray-900">Lifetime Access</p>
                    <p class="text-xs text-gray-500">All 300+ calculators included.</p>
                </div>
                <p class="text-2xl font-black text-gray-900">$4.99</p>
            </div>
            <a href="https://piwatools.lemonsqueezy.com/checkout/buy/95fff32f-9512-4004-9086-886f84ffadcb" target="_blank" class="block text-center bg-green-600 hover:bg-green-700 text-white font-semibold py-2.5 px-4 rounded-lg mt-4 transition shadow-sm">Buy License Key</a>
        </div>
        <div class="space-y-2">
            <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider">Already purchased? Enter License Key</label>
            <div class="flex space-x-2">
                <input type="text" id="licenseKeyInput" placeholder="LK-XXXX-XXXX" class="flex-1 border border-gray-300 rounded-lg px-3 py-2 text-sm uppercase outline-none focus:ring-2 focus:ring-orange-500">
                <button onclick="verifyLicenseKey()" class="bg-gray-900 hover:bg-gray-800 text-white font-medium px-4 py-2 rounded-lg text-sm transition">Activate</button>
            </div>
            <p id="verifyMessage" class="text-xs mt-1"></p>
        </div>
    </div>
</div>

<script>
var CS = "{currency_symbol}";
var REF_RATE = {ref_rate};
var REF_RATE_HIGH = {ref_rate_high};
var REF_THRESHOLD = {ref_threshold};

function calculateProfit() {{
    var price = parseFloat(document.getElementById('sellingPrice').value) || 0;
    var cost = parseFloat(document.getElementById('productCost').value) || 0;
    var shipping = parseFloat(document.getElementById('shippingCost').value) || 0;
    var fbaFee = parseFloat(document.getElementById('fbaFee').value) || 0;
    var ppc = parseFloat(document.getElementById('ppcCost').value) || 0;
    var refFee = 0;
    if (price <= REF_THRESHOLD) {{
        refFee = price * REF_RATE;
    }} else {{
        refFee = REF_THRESHOLD * REF_RATE + (price - REF_THRESHOLD) * REF_RATE_HIGH;
    }}
    var totalExp = cost + shipping + fbaFee + ppc + refFee;
    var profit = price - totalExp;
    var margin = price > 0 ? (profit / price) * 100 : 0;
    var roi = (cost + shipping) > 0 ? (profit / (cost + shipping)) * 100 : 0;
    document.getElementById('referralFeeDisplay').innerText = CS + refFee.toFixed(2);
    document.getElementById('totalExpensesDisplay').innerText = CS + totalExp.toFixed(2);
    document.getElementById('netProfitDisplay').innerText = CS + profit.toFixed(2);
    document.getElementById('marginDisplay').innerText = margin.toFixed(2) + '%';
    document.getElementById('roiDisplay').innerText = roi.toFixed(2) + '%';
    document.getElementById('netProfitDisplay').className = profit >= 0 ? 'text-2xl font-bold text-green-400' : 'text-2xl font-bold text-red-400';
}}
function triggerPaywallAction() {{ var p = localStorage.getItem('is_premium_user') === 'true'; if(p) {{ alert('Generating premium PDF report... (Demo)'); }} else {{ showLicenseModal(); }} }}
function showLicenseModal() {{ document.getElementById('paywallModal').classList.remove('hidden'); }}
function closePaywallModal() {{ document.getElementById('paywallModal').classList.add('hidden'); }}
async function verifyLicenseKey() {{
    var key = document.getElementById('licenseKeyInput').value.trim();
    var el = document.getElementById('verifyMessage');
    if(!key) {{ el.innerText='Please enter a key.'; el.className='text-xs text-red-500 mt-1'; return; }}
    el.innerText='Verifying...'; el.className='text-xs text-yellow-600 mt-1';
    try {{
        var r = await fetch('https://api.lemonsqueezy.com/v1/licenses/activate', {{
            method: 'POST',
            headers: {{ 'Accept':'application/json','Content-Type':'application/json' }},
            body: JSON.stringify({{ license_key: key, instance_name: 'seller-tools-pro' }})
        }});
        var d = await r.json();
        if(d.activated) {{ localStorage.setItem('is_premium_user','true'); el.innerText='License activated! PRO unlocked.'; el.className='text-xs text-green-600 mt-1'; setTimeout(closePaywallModal,1500); }}
        else {{ el.innerText='Invalid license key.'; el.className='text-xs text-red-500 mt-1'; }}
    }} catch(e) {{ el.innerText='Network error. Try again.'; el.className='text-xs text-red-500 mt-1'; }}
}}
calculateProfit();
</script>
</body>
</html>"""


def build_tiktok_html(p, c, cat):
    """TikTok Shop 计算器"""
    symbol = ccy(p["countries"][c])
    country = p["countries"][c]
    plat_name = p["name"]

    # Different commission rates by country
    comm_rates = {"US": 0.06, "UK": 0.05, "ID": 0.04, "TH": 0.04, "VN": 0.03, "MY": 0.04, "PH": 0.04, "SG": 0.05}
    comm_rate = comm_rates.get(country, 0.04)
    comm_rate_str = str(int(comm_rate * 100))

    title = f"{plat_name} {country} {cat_label(cat)} Profit Calculator ({CURRENT_YEAR})"
    desc = f"Calculate your {plat_name} {country} store profit for {cat_label(cat)}. Includes platform commission, affiliate fees, and shipping costs."
    keywords = f"{plat_name} {country} profit calculator, {cat_label(cat)} margin, commission fee {CURRENT_YEAR}"
    h1 = f"{plat_name} {country} Profit Calculator"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <meta name="keywords" content="{keywords}">
    <link rel="stylesheet" href="tailwind.css">
    <style>.blur-overlay{{backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)}}</style>
</head>
<body class="bg-gray-50 text-gray-800 font-sans antialiased">

<header class="bg-white border-b border-gray-200 sticky top-0 z-40 shadow-sm">
    <div class="max-w-5xl mx-auto px-4 py-4 flex justify-between items-center">
        <div class="flex items-center space-x-2">
            <span class="text-2xl">🎵</span>
            <span class="font-bold text-xl tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-yellow-500 to-orange-600">SellerTools Pro</span>
        </div>
        <div class="flex items-center space-x-4">
            <span class="text-xs text-green-600 bg-green-50 px-2.5 py-1 rounded-full font-medium">● {CURRENT_YEAR} Live Rates</span>
            <button onclick="showLicenseModal()" class="text-xs bg-gray-900 hover:bg-gray-800 text-white px-3 py-1.5 rounded-lg font-medium transition">Activate PRO</button>
        </div>
    </div>
</header>

<main class="max-w-5xl mx-auto px-4 py-10 grid grid-cols-1 md:grid-cols-3 gap-8">
    <section class="md:col-span-2 bg-white border border-gray-200 rounded-2xl p-6 shadow-sm">
        <h1 class="text-2xl font-bold text-gray-900 mb-6">{h1} <span class="text-black text-lg">({cat_label_cn(cat)})</span></h1>
        <div class="space-y-6">
            <div>
                <h2 class="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-3">1. Product & Pricing</h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Selling Price ({symbol})</label>
                        <input type="number" id="sellingPrice" value="29.99" class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none transition">
                    </div>
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Product Cost ({symbol})</label>
                        <input type="number" id="productCost" value="8.00" class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none transition">
                    </div>
                </div>
            </div>
            <div>
                <h2 class="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-3">2. Shipping & Fulfillment</h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Shipping Cost ({symbol})</label>
                        <input type="number" id="shippingCost" value="4.50" class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none transition">
                    </div>
                </div>
            </div>
            <div>
                <h2 class="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-3">3. Commission & Marketing</h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Affiliate Commission %</label>
                        <input type="number" id="affiliatePct" value="10" class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none transition">
                    </div>
                </div>
            </div>
            <button onclick="calculateProfit()" class="w-full bg-gradient-to-r from-yellow-500 to-orange-600 hover:from-yellow-600 hover:to-orange-700 text-white font-semibold py-3 px-4 rounded-xl shadow-md transition transform active:scale-95">Calculate Profit</button>
        </div>
    </section>

    <section class="bg-gray-900 text-white rounded-2xl p-6 shadow-xl flex flex-col justify-between relative overflow-hidden">
        <div>
            <h2 class="text-lg font-bold tracking-tight text-gray-300 mb-6">Financial Summary</h2>
            <div class="space-y-4">
                <div class="flex justify-between border-b border-gray-800 pb-2">
                    <span class="text-gray-400">Platform Commission ({comm_rate_str}%)</span>
                    <span id="platformFeeDisplay" class="font-medium">{symbol}0.00</span>
                </div>
                <div class="flex justify-between border-b border-gray-800 pb-2">
                    <span class="text-gray-400">Affiliate Commission</span>
                    <span id="affiliateFeeDisplay" class="font-medium">{symbol}0.00</span>
                </div>
                <div class="flex justify-between border-b border-gray-800 pb-2">
                    <span class="text-gray-400">Total Expenses</span>
                    <span id="totalExpensesDisplay" class="font-medium">{symbol}0.00</span>
                </div>
                <div class="flex justify-between pt-2">
                    <span class="text-gray-200 font-semibold text-lg">Net Profit</span>
                    <span id="netProfitDisplay" class="text-2xl font-bold text-green-400">{symbol}0.00</span>
                </div>
                <div class="flex justify-between">
                    <span class="text-gray-400">Net Margin</span>
                    <span id="marginDisplay" class="font-medium text-green-400">0.00%</span>
                </div>
            </div>
        </div>
        <div class="mt-8 pt-6 border-t border-gray-800">
            <button onclick="triggerPaywallAction()" class="w-full bg-yellow-500 hover:bg-yellow-400 text-gray-950 font-bold py-3 px-4 rounded-xl flex items-center justify-center space-x-2 transition shadow-lg">
                <span>📊</span>
                <span>Export Premium PDF Report</span>
            </button>
            <p class="text-center text-xs text-gray-500 mt-2">🔒 Pro feature. Requires activation key.</p>
        </div>
    </section>
</main>

<div id="paywallModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 bg-gray-950 bg-opacity-60 blur-overlay">
    <div class="bg-white rounded-2xl max-w-md w-full p-6 shadow-2xl relative border border-gray-100 text-gray-800">
        <button onclick="closePaywallModal()" class="absolute top-4 right-4 text-gray-400 hover:text-gray-600 text-xl" style="background:none;border:none;cursor:pointer;">&times;</button>
        <div class="text-center mb-6">
            <span class="text-4xl">💎</span>
            <h3 class="text-xl font-bold text-gray-900 mt-2">Unlock Premium</h3>
            <p class="text-sm text-gray-500 mt-1">Export professional PDF reports.</p>
        </div>
        <div class="bg-gray-50 rounded-xl p-4 mb-6 border border-gray-200">
            <div class="flex justify-between items-center">
                <div><p class="font-semibold text-gray-900">Lifetime Access</p><p class="text-xs text-gray-500">All calculators included.</p></div>
                <p class="text-2xl font-black text-gray-900">$4.99</p>
            </div>
            <a href="https://piwatools.lemonsqueezy.com/checkout/buy/95fff32f-9512-4004-9086-886f84ffadcb" target="_blank" class="block text-center bg-green-600 hover:bg-green-700 text-white font-semibold py-2.5 px-4 rounded-lg mt-4 transition shadow-sm">Buy License Key</a>
        </div>
        <div class="space-y-2">
            <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider">License Key</label>
            <div class="flex space-x-2">
                <input type="text" id="licenseKeyInput" placeholder="LK-XXXX-XXXX" class="flex-1 border border-gray-300 rounded-lg px-3 py-2 text-sm uppercase outline-none focus:ring-2 focus:ring-orange-500">
                <button onclick="verifyLicenseKey()" class="bg-gray-900 hover:bg-gray-800 text-white font-medium px-4 py-2 rounded-lg text-sm transition">Activate</button>
            </div>
            <p id="verifyMessage" class="text-xs mt-1"></p>
        </div>
    </div>
</div>

<script>
var CS = "{symbol}";
var COMM_RATE = {comm_rate};
var country = "{country}";

function calculateProfit() {{
    var price = parseFloat(document.getElementById('sellingPrice').value) || 0;
    var cost = parseFloat(document.getElementById('productCost').value) || 0;
    var shipping = parseFloat(document.getElementById('shippingCost').value) || 0;
    var affPct = parseFloat(document.getElementById('affiliatePct').value) || 0;
    var platformFee = price * COMM_RATE;
    var affiliateFee = price * (affPct / 100);
    var totalExp = cost + shipping + platformFee + affiliateFee;
    var profit = price - totalExp;
    var margin = price > 0 ? (profit / price) * 100 : 0;
    document.getElementById('platformFeeDisplay').innerText = CS + platformFee.toFixed(2);
    document.getElementById('affiliateFeeDisplay').innerText = CS + affiliateFee.toFixed(2);
    document.getElementById('totalExpensesDisplay').innerText = CS + totalExp.toFixed(2);
    document.getElementById('netProfitDisplay').innerText = CS + profit.toFixed(2);
    document.getElementById('marginDisplay').innerText = margin.toFixed(2) + '%';
    document.getElementById('netProfitDisplay').className = profit >= 0 ? 'text-2xl font-bold text-green-400' : 'text-2xl font-bold text-red-400';
}}
function triggerPaywallAction() {{ var p = localStorage.getItem('is_premium_user') === 'true'; if(p) {{ alert('Generating premium PDF report... (Demo)'); }} else {{ showLicenseModal(); }} }}
function showLicenseModal() {{ document.getElementById('paywallModal').classList.remove('hidden'); }}
function closePaywallModal() {{ document.getElementById('paywallModal').classList.add('hidden'); }}
async function verifyLicenseKey() {{
    var key = document.getElementById('licenseKeyInput').value.trim();
    var el = document.getElementById('verifyMessage');
    if(!key) {{ el.innerText='Please enter a key.'; el.className='text-xs text-red-500 mt-1'; return; }}
    el.innerText='Verifying...'; el.className='text-xs text-yellow-600 mt-1';
    try {{
        var r = await fetch('https://api.lemonsqueezy.com/v1/licenses/activate', {{
            method: 'POST',
            headers: {{ 'Accept':'application/json','Content-Type':'application/json' }},
            body: JSON.stringify({{ license_key: key, instance_name: 'seller-tools-pro' }})
        }});
        var d = await r.json();
        if(d.activated) {{ localStorage.setItem('is_premium_user','true'); el.innerText='License activated! PRO unlocked.'; el.className='text-xs text-green-600 mt-1'; setTimeout(closePaywallModal,1500); }}
        else {{ el.innerText='Invalid license key.'; el.className='text-xs text-red-500 mt-1'; }}
    }} catch(e) {{ el.innerText='Network error. Try again.'; el.className='text-xs text-red-500 mt-1'; }}
}}
calculateProfit();
</script>
</body>
</html>"""


def build_shopify_html(p, c, cat):
    """Shopify 计算器"""
    country = p["countries"][c]
    symbol = ccy(country)
    plat_name = p["name"]
    # Shopify fee: Basic 2.9%+$0.30, Shopify 2.6%+$0.30, Advanced 2.4%+$0.30
    title = f"{plat_name} {country} {cat_label(cat)} Profit Calculator ({CURRENT_YEAR})"
    desc = f"Calculate your {plat_name} store profit for {cat_label(cat)}. Includes transaction fees, payment processing, and shipping costs."
    keywords = f"{plat_name} {country} profit calculator, {cat_label(cat)} margin, transaction fee {CURRENT_YEAR}"
    h1 = f"{plat_name} {country} Profit Calculator"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <meta name="keywords" content="{keywords}">
    <link rel="stylesheet" href="tailwind.css">
    <style>.blur-overlay{{backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)}}</style>
</head>
<body class="bg-gray-50 text-gray-800 font-sans antialiased">

<header class="bg-white border-b border-gray-200 sticky top-0 z-40 shadow-sm">
    <div class="max-w-5xl mx-auto px-4 py-4 flex justify-between items-center">
        <div class="flex items-center space-x-2">
            <span class="text-2xl">🛍️</span>
            <span class="font-bold text-xl tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-yellow-500 to-orange-600">SellerTools Pro</span>
        </div>
        <div class="flex items-center space-x-4">
            <span class="text-xs text-green-600 bg-green-50 px-2.5 py-1 rounded-full font-medium">● {CURRENT_YEAR} Live Rates</span>
            <button onclick="showLicenseModal()" class="text-xs bg-gray-900 hover:bg-gray-800 text-white px-3 py-1.5 rounded-lg font-medium transition">Activate PRO</button>
        </div>
    </div>
</header>

<main class="max-w-5xl mx-auto px-4 py-10 grid grid-cols-1 md:grid-cols-3 gap-8">
    <section class="md:col-span-2 bg-white border border-gray-200 rounded-2xl p-6 shadow-sm">
        <h1 class="text-2xl font-bold text-gray-900 mb-6">{h1} <span class="text-emerald-600 text-lg">({cat_label_cn(cat)})</span></h1>
        <div class="space-y-6">
            <div>
                <h2 class="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-3">1. Product & Pricing</h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Selling Price ({symbol})</label>
                        <input type="number" id="sellingPrice" value="39.99" class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none transition">
                    </div>
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Product Cost ({symbol})</label>
                        <input type="number" id="productCost" value="15.00" class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none transition">
                    </div>
                </div>
            </div>
            <div>
                <h2 class="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-3">2. Shipping & Fulfillment</h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Shipping Cost ({symbol})</label>
                        <input type="number" id="shippingCost" value="5.00" class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none transition">
                    </div>
                </div>
            </div>
            <div>
                <h2 class="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-3">3. Shopify Plan</h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Plan</label>
                        <select id="planType" class="w-full border border-gray-300 rounded-xl px-4 py-2.5 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none transition bg-white">
                            <option value="basic">Basic ({symbol}2.9% + {symbol}0.30)</option>
                            <option value="shopify">Shopify ({symbol}2.6% + {symbol}0.30)</option>
                            <option value="advanced">Advanced ({symbol}2.4% + {symbol}0.30)</option>
                        </select>
                    </div>
                </div>
            </div>
            <button onclick="calculateProfit()" class="w-full bg-gradient-to-r from-yellow-500 to-orange-600 hover:from-yellow-600 hover:to-orange-700 text-white font-semibold py-3 px-4 rounded-xl shadow-md transition transform active:scale-95">Calculate Profit</button>
        </div>
    </section>

    <section class="bg-gray-900 text-white rounded-2xl p-6 shadow-xl flex flex-col justify-between relative overflow-hidden">
        <div>
            <h2 class="text-lg font-bold tracking-tight text-gray-300 mb-6">Financial Summary</h2>
            <div class="space-y-4">
                <div class="flex justify-between border-b border-gray-800 pb-2">
                    <span class="text-gray-400">Transaction Fee</span>
                    <span id="txFeeDisplay" class="font-medium">{symbol}0.00</span>
                </div>
                <div class="flex justify-between border-b border-gray-800 pb-2">
                    <span class="text-gray-400">Total Expenses</span>
                    <span id="totalExpensesDisplay" class="font-medium">{symbol}0.00</span>
                </div>
                <div class="flex justify-between pt-2">
                    <span class="text-gray-200 font-semibold text-lg">Net Profit</span>
                    <span id="netProfitDisplay" class="text-2xl font-bold text-green-400">{symbol}0.00</span>
                </div>
                <div class="flex justify-between">
                    <span class="text-gray-400">Net Margin</span>
                    <span id="marginDisplay" class="font-medium text-green-400">0.00%</span>
                </div>
            </div>
        </div>
        <div class="mt-8 pt-6 border-t border-gray-800">
            <button onclick="triggerPaywallAction()" class="w-full bg-yellow-500 hover:bg-yellow-400 text-gray-950 font-bold py-3 px-4 rounded-xl flex items-center justify-center space-x-2 transition shadow-lg">
                <span>📊</span>
                <span>Export Premium PDF Report</span>
            </button>
            <p class="text-center text-xs text-gray-500 mt-2">🔒 Pro feature. Requires activation key.</p>
        </div>
    </section>
</main>

<div id="paywallModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 bg-gray-950 bg-opacity-60 blur-overlay">
    <div class="bg-white rounded-2xl max-w-md w-full p-6 shadow-2xl relative border border-gray-100 text-gray-800">
        <button onclick="closePaywallModal()" class="absolute top-4 right-4 text-gray-400 hover:text-gray-600 text-xl" style="background:none;border:none;cursor:pointer;">&times;</button>
        <div class="text-center mb-6">
            <span class="text-4xl">💎</span>
            <h3 class="text-xl font-bold text-gray-900 mt-2">Unlock Premium</h3>
            <p class="text-sm text-gray-500 mt-1">Export professional PDF reports.</p>
        </div>
        <div class="bg-gray-50 rounded-xl p-4 mb-6 border border-gray-200">
            <div class="flex justify-between items-center">
                <div><p class="font-semibold text-gray-900">Lifetime Access</p><p class="text-xs text-gray-500">All calculators included.</p></div>
                <p class="text-2xl font-black text-gray-900">$4.99</p>
            </div>
            <a href="https://piwatools.lemonsqueezy.com/checkout/buy/95fff32f-9512-4004-9086-886f84ffadcb" target="_blank" class="block text-center bg-green-600 hover:bg-green-700 text-white font-semibold py-2.5 px-4 rounded-lg mt-4 transition shadow-sm">Buy License Key</a>
        </div>
        <div class="space-y-2">
            <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider">License Key</label>
            <div class="flex space-x-2">
                <input type="text" id="licenseKeyInput" placeholder="LK-XXXX-XXXX" class="flex-1 border border-gray-300 rounded-lg px-3 py-2 text-sm uppercase outline-none focus:ring-2 focus:ring-orange-500">
                <button onclick="verifyLicenseKey()" class="bg-gray-900 hover:bg-gray-800 text-white font-medium px-4 py-2 rounded-lg text-sm transition">Activate</button>
            </div>
            <p id="verifyMessage" class="text-xs mt-1"></p>
        </div>
    </div>
</div>

<script>
var CS = "{symbol}";

function calculateProfit() {{
    var price = parseFloat(document.getElementById('sellingPrice').value) || 0;
    var cost = parseFloat(document.getElementById('productCost').value) || 0;
    var shipping = parseFloat(document.getElementById('shippingCost').value) || 0;
    var plan = document.getElementById('planType').value;
    var rates = {{'basic': [0.029, 0.30], 'shopify': [0.026, 0.30], 'advanced': [0.024, 0.30]}};
    var r = rates[plan] || rates['basic'];
    var txFee = price * r[0] + r[1];
    var totalExp = cost + shipping + txFee;
    var profit = price - totalExp;
    var margin = price > 0 ? (profit / price) * 100 : 0;
    document.getElementById('txFeeDisplay').innerText = CS + txFee.toFixed(2);
    document.getElementById('totalExpensesDisplay').innerText = CS + totalExp.toFixed(2);
    document.getElementById('netProfitDisplay').innerText = CS + profit.toFixed(2);
    document.getElementById('marginDisplay').innerText = margin.toFixed(2) + '%';
    document.getElementById('netProfitDisplay').className = profit >= 0 ? 'text-2xl font-bold text-green-400' : 'text-2xl font-bold text-red-400';
}}
function triggerPaywallAction() {{ var p = localStorage.getItem('is_premium_user') === 'true'; if(p) {{ alert('Generating premium PDF report... (Demo)'); }} else {{ showLicenseModal(); }} }}
function showLicenseModal() {{ document.getElementById('paywallModal').classList.remove('hidden'); }}
function closePaywallModal() {{ document.getElementById('paywallModal').classList.add('hidden'); }}
async function verifyLicenseKey() {{
    var key = document.getElementById('licenseKeyInput').value.trim();
    var el = document.getElementById('verifyMessage');
    if(!key) {{ el.innerText='Please enter a key.'; el.className='text-xs text-red-500 mt-1'; return; }}
    el.innerText='Verifying...'; el.className='text-xs text-yellow-600 mt-1';
    try {{
        var r = await fetch('https://api.lemonsqueezy.com/v1/licenses/activate', {{
            method: 'POST',
            headers: {{ 'Accept':'application/json','Content-Type':'application/json' }},
            body: JSON.stringify({{ license_key: key, instance_name: 'seller-tools-pro' }})
        }});
        var d = await r.json();
        if(d.activated) {{ localStorage.setItem('is_premium_user','true'); el.innerText='License activated! PRO unlocked.'; el.className='text-xs text-green-600 mt-1'; setTimeout(closePaywallModal,1500); }}
        else {{ el.innerText='Invalid license key.'; el.className='text-xs text-red-500 mt-1'; }}
    }} catch(e) {{ el.innerText='Network error. Try again.'; el.className='text-xs text-red-500 mt-1'; }}
}}
calculateProfit();
</script>
</body>
</html>"""


def build_etsy_html(p, c, cat):
    """Etsy 计算器"""
    country = p["countries"][c]
    symbol = ccy(country)
    plat_name = p["name"]
    title = f"{plat_name} {country} {cat_label(cat)} Profit Calculator ({CURRENT_YEAR})"
    desc = f"Calculate your {plat_name} shop profit for {cat_label(cat)}. Includes transaction fees, listing fees, and payment processing."
    keywords = f"{plat_name} {country} profit calculator, {cat_label(cat)} margin, Etsy fee {CURRENT_YEAR}"
    h1 = f"{plat_name} {country} Profit Calculator"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <meta name="keywords" content="{keywords}">
    <link rel="stylesheet" href="tailwind.css">
    <style>.blur-overlay{{backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)}}</style>
</head>
<body class="bg-gray-50 text-gray-800 font-sans antialiased">

<header class="bg-white border-b border-gray-200 sticky top-0 z-40 shadow-sm">
    <div class="max-w-5xl mx-auto px-4 py-4 flex justify-between items-center">
        <div class="flex items-center space-x-2">
            <span class="text-2xl">🧶</span>
            <span class="font-bold text-xl tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-yellow-500 to-orange-600">SellerTools Pro</span>
        </div>
        <div class="flex items-center space-x-4">
            <span class="text-xs text-green-600 bg-green-50 px-2.5 py-1 rounded-full font-medium">● {CURRENT_YEAR} Live Rates</span>
            <button onclick="showLicenseModal()" class="text-xs bg-gray-900 hover:bg-gray-800 text-white px-3 py-1.5 rounded-lg font-medium transition">Activate PRO</button>
        </div>
    </div>
</header>

<main class="max-w-5xl mx-auto px-4 py-10 grid grid-cols-1 md:grid-cols-3 gap-8">
    <section class="md:col-span-2 bg-white border border-gray-200 rounded-2xl p-6 shadow-sm">
        <h1 class="text-2xl font-bold text-gray-900 mb-6">{h1} <span class="text-amber-600 text-lg">({cat_label_cn(cat)})</span></h1>
        <div class="space-y-6">
            <div>
                <h2 class="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-3">1. Product & Pricing</h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Selling Price ({symbol})</label>
                        <input type="number" id="sellingPrice" value="45.00" class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none transition">
                    </div>
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Material & Labor Cost ({symbol})</label>
                        <input type="number" id="productCost" value="18.00" class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none transition">
                    </div>
                </div>
            </div>
            <div>
                <h2 class="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-3">2. Shipping</h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Shipping Cost ({symbol})</label>
                        <input type="number" id="shippingCost" value="6.00" class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none transition">
                    </div>
                </div>
            </div>
            <div>
                <h2 class="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-3">3. Additional</h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Number of Items</label>
                        <input type="number" id="itemCount" value="1" min="1" class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none transition">
                    </div>
                    <div class="mb-4 flex items-center pt-6">
                        <label class="flex items-center space-x-2 cursor-pointer">
                            <input type="checkbox" id="offsiteAds" class="w-4 h-4 text-orange-500 border-gray-300 rounded focus:ring-orange-500">
                            <span class="text-sm text-gray-700">Include offsite ads fee (15%)</span>
                        </label>
                    </div>
                </div>
            </div>
            <button onclick="calculateProfit()" class="w-full bg-gradient-to-r from-yellow-500 to-orange-600 hover:from-yellow-600 hover:to-orange-700 text-white font-semibold py-3 px-4 rounded-xl shadow-md transition transform active:scale-95">Calculate Profit</button>
        </div>
    </section>

    <section class="bg-gray-900 text-white rounded-2xl p-6 shadow-xl flex flex-col justify-between relative overflow-hidden">
        <div>
            <h2 class="text-lg font-bold tracking-tight text-gray-300 mb-6">Financial Summary</h2>
            <div class="space-y-4">
                <div class="flex justify-between border-b border-gray-800 pb-2">
                    <span class="text-gray-400">Listing Fee</span>
                    <span id="listingFeeDisplay" class="font-medium">{symbol}0.00</span>
                </div>
                <div class="flex justify-between border-b border-gray-800 pb-2">
                    <span class="text-gray-400">Transaction Fee (6.5%)</span>
                    <span id="txFeeDisplay" class="font-medium">{symbol}0.00</span>
                </div>
                <div class="flex justify-between border-b border-gray-800 pb-2">
                    <span class="text-gray-400">Payment Processing</span>
                    <span id="paymentFeeDisplay" class="font-medium">{symbol}0.00</span>
                </div>
                <div class="flex justify-between border-b border-gray-800 pb-2">
                    <span class="text-gray-400">Offsite Ads Fee</span>
                    <span id="offsiteFeeDisplay" class="font-medium">{symbol}0.00</span>
                </div>
                <div class="flex justify-between border-b border-gray-800 pb-2">
                    <span class="text-gray-400">Total Expenses</span>
                    <span id="totalExpensesDisplay" class="font-medium">{symbol}0.00</span>
                </div>
                <div class="flex justify-between pt-2">
                    <span class="text-gray-200 font-semibold text-lg">Net Profit</span>
                    <span id="netProfitDisplay" class="text-2xl font-bold text-green-400">{symbol}0.00</span>
                </div>
                <div class="flex justify-between">
                    <span class="text-gray-400">Net Margin</span>
                    <span id="marginDisplay" class="font-medium text-green-400">0.00%</span>
                </div>
            </div>
        </div>
        <div class="mt-8 pt-6 border-t border-gray-800">
            <button onclick="triggerPaywallAction()" class="w-full bg-yellow-500 hover:bg-yellow-400 text-gray-950 font-bold py-3 px-4 rounded-xl flex items-center justify-center space-x-2 transition shadow-lg">
                <span>📊</span>
                <span>Export Premium PDF Report</span>
            </button>
            <p class="text-center text-xs text-gray-500 mt-2">🔒 Pro feature. Requires activation key.</p>
        </div>
    </section>
</main>

<div id="paywallModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 bg-gray-950 bg-opacity-60 blur-overlay">
    <div class="bg-white rounded-2xl max-w-md w-full p-6 shadow-2xl relative border border-gray-100 text-gray-800">
        <button onclick="closePaywallModal()" class="absolute top-4 right-4 text-gray-400 hover:text-gray-600 text-xl" style="background:none;border:none;cursor:pointer;">&times;</button>
        <div class="text-center mb-6">
            <span class="text-4xl">💎</span>
            <h3 class="text-xl font-bold text-gray-900 mt-2">Unlock Premium</h3>
            <p class="text-sm text-gray-500 mt-1">Export professional PDF reports.</p>
        </div>
        <div class="bg-gray-50 rounded-xl p-4 mb-6 border border-gray-200">
            <div class="flex justify-between items-center">
                <div><p class="font-semibold text-gray-900">Lifetime Access</p><p class="text-xs text-gray-500">All calculators included.</p></div>
                <p class="text-2xl font-black text-gray-900">$4.99</p>
            </div>
            <a href="https://piwatools.lemonsqueezy.com/checkout/buy/95fff32f-9512-4004-9086-886f84ffadcb" target="_blank" class="block text-center bg-green-600 hover:bg-green-700 text-white font-semibold py-2.5 px-4 rounded-lg mt-4 transition shadow-sm">Buy License Key</a>
        </div>
        <div class="space-y-2">
            <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider">License Key</label>
            <div class="flex space-x-2">
                <input type="text" id="licenseKeyInput" placeholder="LK-XXXX-XXXX" class="flex-1 border border-gray-300 rounded-lg px-3 py-2 text-sm uppercase outline-none focus:ring-2 focus:ring-orange-500">
                <button onclick="verifyLicenseKey()" class="bg-gray-900 hover:bg-gray-800 text-white font-medium px-4 py-2 rounded-lg text-sm transition">Activate</button>
            </div>
            <p id="verifyMessage" class="text-xs mt-1"></p>
        </div>
    </div>
</div>

<script>
var CS = "{symbol}";

function calculateProfit() {{
    var price = parseFloat(document.getElementById('sellingPrice').value) || 0;
    var cost = parseFloat(document.getElementById('productCost').value) || 0;
    var shipping = parseFloat(document.getElementById('shippingCost').value) || 0;
    var items = parseInt(document.getElementById('itemCount').value) || 1;
    var hasAds = document.getElementById('offsiteAds').checked;
    var listingFee = items * 0.20;
    var txFee = price * 0.065;
    var paymentFee = price * 0.03 + 0.25;
    var adsFee = hasAds ? price * 0.15 : 0;
    var totalExp = cost + shipping + listingFee + txFee + paymentFee + adsFee;
    var profit = price - totalExp;
    var margin = price > 0 ? (profit / price) * 100 : 0;
    document.getElementById('listingFeeDisplay').innerText = CS + listingFee.toFixed(2);
    document.getElementById('txFeeDisplay').innerText = CS + txFee.toFixed(2);
    document.getElementById('paymentFeeDisplay').innerText = CS + paymentFee.toFixed(2);
    document.getElementById('offsiteFeeDisplay').innerText = CS + adsFee.toFixed(2);
    document.getElementById('totalExpensesDisplay').innerText = CS + totalExp.toFixed(2);
    document.getElementById('netProfitDisplay').innerText = CS + profit.toFixed(2);
    document.getElementById('marginDisplay').innerText = margin.toFixed(2) + '%';
    document.getElementById('netProfitDisplay').className = profit >= 0 ? 'text-2xl font-bold text-green-400' : 'text-2xl font-bold text-red-400';
}}
function triggerPaywallAction() {{ var p = localStorage.getItem('is_premium_user') === 'true'; if(p) {{ alert('Generating premium PDF report... (Demo)'); }} else {{ showLicenseModal(); }} }}
function showLicenseModal() {{ document.getElementById('paywallModal').classList.remove('hidden'); }}
function closePaywallModal() {{ document.getElementById('paywallModal').classList.add('hidden'); }}
async function verifyLicenseKey() {{
    var key = document.getElementById('licenseKeyInput').value.trim();
    var el = document.getElementById('verifyMessage');
    if(!key) {{ el.innerText='Please enter a key.'; el.className='text-xs text-red-500 mt-1'; return; }}
    el.innerText='Verifying...'; el.className='text-xs text-yellow-600 mt-1';
    try {{
        var r = await fetch('https://api.lemonsqueezy.com/v1/licenses/activate', {{
            method: 'POST',
            headers: {{ 'Accept':'application/json','Content-Type':'application/json' }},
            body: JSON.stringify({{ license_key: key, instance_name: 'seller-tools-pro' }})
        }});
        var d = await r.json();
        if(d.activated) {{ localStorage.setItem('is_premium_user','true'); el.innerText='License activated! PRO unlocked.'; el.className='text-xs text-green-600 mt-1'; setTimeout(closePaywallModal,1500); }}
        else {{ el.innerText='Invalid license key.'; el.className='text-xs text-red-500 mt-1'; }}
    }} catch(e) {{ el.innerText='Network error. Try again.'; el.className='text-xs text-red-500 mt-1'; }}
}}
calculateProfit();
</script>
</body>
</html>"""


def build_ebay_html(p, c, cat):
    """eBay 计算器"""
    country = p["countries"][c]
    symbol = ccy(country)
    plat_name = p["name"]
    title = f"{plat_name} {country} {cat_label(cat)} Profit Calculator ({CURRENT_YEAR})"
    desc = f"Calculate your {plat_name} {country} selling profit for {cat_label(cat)}. Includes insertion fees, final value fees, and promoted listing costs."
    keywords = f"{plat_name} {country} calculator, {cat_label(cat)} profit calculator, final value fee {CURRENT_YEAR}"
    h1 = f"{plat_name} {country} Profit Calculator"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <meta name="keywords" content="{keywords}">
    <link rel="stylesheet" href="tailwind.css">
    <style>.blur-overlay{{backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)}}</style>
</head>
<body class="bg-gray-50 text-gray-800 font-sans antialiased">

<header class="bg-white border-b border-gray-200 sticky top-0 z-40 shadow-sm">
    <div class="max-w-5xl mx-auto px-4 py-4 flex justify-between items-center">
        <div class="flex items-center space-x-2">
            <span class="text-2xl">📦</span>
            <span class="font-bold text-xl tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-yellow-500 to-orange-600">SellerTools Pro</span>
        </div>
        <div class="flex items-center space-x-4">
            <span class="text-xs text-green-600 bg-green-50 px-2.5 py-1 rounded-full font-medium">● {CURRENT_YEAR} Live Rates</span>
            <button onclick="showLicenseModal()" class="text-xs bg-gray-900 hover:bg-gray-800 text-white px-3 py-1.5 rounded-lg font-medium transition">Activate PRO</button>
        </div>
    </div>
</header>

<main class="max-w-5xl mx-auto px-4 py-10 grid grid-cols-1 md:grid-cols-3 gap-8">
    <section class="md:col-span-2 bg-white border border-gray-200 rounded-2xl p-6 shadow-sm">
        <h1 class="text-2xl font-bold text-gray-900 mb-6">{h1} <span class="text-blue-600 text-lg">({cat_label_cn(cat)})</span></h1>
        <div class="space-y-6">
            <div>
                <h2 class="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-3">1. Sale Details</h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Sale Price ({symbol})</label>
                        <input type="number" id="sellingPrice" value="99.99" class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none transition">
                    </div>
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Product Cost ({symbol})</label>
                        <input type="number" id="productCost" value="35.00" class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none transition">
                    </div>
                </div>
            </div>
            <div>
                <h2 class="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-3">2. Shipping & Costs</h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Shipping Cost ({symbol})</label>
                        <input type="number" id="shippingCost" value="8.50" class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none transition">
                    </div>
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Promoted Rate (%)</label>
                        <input type="number" id="promotedRate" value="0" class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none transition">
                    </div>
                </div>
            </div>
            <div class="flex items-center space-x-3 mb-4">
                <label class="flex items-center space-x-2 cursor-pointer">
                    <input type="checkbox" id="internationalBuyer" class="w-4 h-4 text-orange-500 border-gray-300 rounded focus:ring-orange-500">
                    <span class="text-sm text-gray-700">International buyer (+1.65% fee)</span>
                </label>
            </div>
            <button onclick="calculateProfit()" class="w-full bg-gradient-to-r from-yellow-500 to-orange-600 hover:from-yellow-600 hover:to-orange-700 text-white font-semibold py-3 px-4 rounded-xl shadow-md transition transform active:scale-95">Calculate Profit</button>
        </div>
    </section>

    <section class="bg-gray-900 text-white rounded-2xl p-6 shadow-xl flex flex-col justify-between relative overflow-hidden">
        <div>
            <h2 class="text-lg font-bold tracking-tight text-gray-300 mb-6">Financial Summary</h2>
            <div class="space-y-4">
                <div class="flex justify-between border-b border-gray-800 pb-2">
                    <span class="text-gray-400">Insertion Fee</span>
                    <span id="insertionFeeDisplay" class="font-medium">{symbol}0.00</span>
                </div>
                <div class="flex justify-between border-b border-gray-800 pb-2">
                    <span class="text-gray-400">Final Value Fee (13.25%)</span>
                    <span id="finalFeeDisplay" class="font-medium">{symbol}0.00</span>
                </div>
                <div class="flex justify-between border-b border-gray-800 pb-2">
                    <span class="text-gray-400">International Fee</span>
                    <span id="intlFeeDisplay" class="font-medium">{symbol}0.00</span>
                </div>
                <div class="flex justify-between border-b border-gray-800 pb-2">
                    <span class="text-gray-400">Promoted Fee</span>
                    <span id="promotedFeeDisplay" class="font-medium">{symbol}0.00</span>
                </div>
                <div class="flex justify-between border-b border-gray-800 pb-2">
                    <span class="text-gray-400">Total Expenses</span>
                    <span id="totalExpensesDisplay" class="font-medium">{symbol}0.00</span>
                </div>
                <div class="flex justify-between pt-2">
                    <span class="text-gray-200 font-semibold text-lg">Net Profit</span>
                    <span id="netProfitDisplay" class="text-2xl font-bold text-green-400">{symbol}0.00</span>
                </div>
                <div class="flex justify-between">
                    <span class="text-gray-400">Net Margin</span>
                    <span id="marginDisplay" class="font-medium text-green-400">0.00%</span>
                </div>
            </div>
        </div>
        <div class="mt-8 pt-6 border-t border-gray-800">
            <button onclick="triggerPaywallAction()" class="w-full bg-yellow-500 hover:bg-yellow-400 text-gray-950 font-bold py-3 px-4 rounded-xl flex items-center justify-center space-x-2 transition shadow-lg">
                <span>📊</span>
                <span>Export Premium PDF Report</span>
            </button>
            <p class="text-center text-xs text-gray-500 mt-2">🔒 Pro feature. Requires activation key.</p>
        </div>
    </section>
</main>

<div id="paywallModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 bg-gray-950 bg-opacity-60 blur-overlay">
    <div class="bg-white rounded-2xl max-w-md w-full p-6 shadow-2xl relative border border-gray-100 text-gray-800">
        <button onclick="closePaywallModal()" class="absolute top-4 right-4 text-gray-400 hover:text-gray-600 text-xl" style="background:none;border:none;cursor:pointer;">&times;</button>
        <div class="text-center mb-6">
            <span class="text-4xl">💎</span>
            <h3 class="text-xl font-bold text-gray-900 mt-2">Unlock Premium</h3>
            <p class="text-sm text-gray-500 mt-1">Export professional PDF reports.</p>
        </div>
        <div class="bg-gray-50 rounded-xl p-4 mb-6 border border-gray-200">
            <div class="flex justify-between items-center">
                <div><p class="font-semibold text-gray-900">Lifetime Access</p><p class="text-xs text-gray-500">All calculators included.</p></div>
                <p class="text-2xl font-black text-gray-900">$4.99</p>
            </div>
            <a href="https://piwatools.lemonsqueezy.com/checkout/buy/95fff32f-9512-4004-9086-886f84ffadcb" target="_blank" class="block text-center bg-green-600 hover:bg-green-700 text-white font-semibold py-2.5 px-4 rounded-lg mt-4 transition shadow-sm">Buy License Key</a>
        </div>
        <div class="space-y-2">
            <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider">License Key</label>
            <div class="flex space-x-2">
                <input type="text" id="licenseKeyInput" placeholder="LK-XXXX-XXXX" class="flex-1 border border-gray-300 rounded-lg px-3 py-2 text-sm uppercase outline-none focus:ring-2 focus:ring-orange-500">
                <button onclick="verifyLicenseKey()" class="bg-gray-900 hover:bg-gray-800 text-white font-medium px-4 py-2 rounded-lg text-sm transition">Activate</button>
            </div>
            <p id="verifyMessage" class="text-xs mt-1"></p>
        </div>
    </div>
</div>

<script>
var CS = "{symbol}";

function calculateProfit() {{
    var price = parseFloat(document.getElementById('sellingPrice').value) || 0;
    var cost = parseFloat(document.getElementById('productCost').value) || 0;
    var shipping = parseFloat(document.getElementById('shippingCost').value) || 0;
    var promotedPct = parseFloat(document.getElementById('promotedRate').value) || 0;
    var isIntl = document.getElementById('internationalBuyer').checked;
    var insertion = 0.35;
    var finalVal = 0;
    if (price <= 7500) {{ finalVal = price * 0.1325; }} else {{ finalVal = 7500 * 0.1325 + (price - 7500) * 0.0235; }}
    var intlFee = isIntl ? price * 0.0165 : 0;
    var promotedFee = price * (promotedPct / 100);
    var totalExp = cost + shipping + insertion + finalVal + intlFee + promotedFee;
    var profit = price - totalExp;
    var margin = price > 0 ? (profit / price) * 100 : 0;
    document.getElementById('insertionFeeDisplay').innerText = CS + insertion.toFixed(2);
    document.getElementById('finalFeeDisplay').innerText = CS + finalVal.toFixed(2);
    document.getElementById('intlFeeDisplay').innerText = CS + intlFee.toFixed(2);
    document.getElementById('promotedFeeDisplay').innerText = CS + promotedFee.toFixed(2);
    document.getElementById('totalExpensesDisplay').innerText = CS + totalExp.toFixed(2);
    document.getElementById('netProfitDisplay').innerText = CS + profit.toFixed(2);
    document.getElementById('marginDisplay').innerText = margin.toFixed(2) + '%';
    document.getElementById('netProfitDisplay').className = profit >= 0 ? 'text-2xl font-bold text-green-400' : 'text-2xl font-bold text-red-400';
}}
function triggerPaywallAction() {{ var p = localStorage.getItem('is_premium_user') === 'true'; if(p) {{ alert('Generating premium PDF report... (Demo)'); }} else {{ showLicenseModal(); }} }}
function showLicenseModal() {{ document.getElementById('paywallModal').classList.remove('hidden'); }}
function closePaywallModal() {{ document.getElementById('paywallModal').classList.add('hidden'); }}
async function verifyLicenseKey() {{
    var key = document.getElementById('licenseKeyInput').value.trim();
    var el = document.getElementById('verifyMessage');
    if(!key) {{ el.innerText='Please enter a key.'; el.className='text-xs text-red-500 mt-1'; return; }}
    el.innerText='Verifying...'; el.className='text-xs text-yellow-600 mt-1';
    try {{
        var r = await fetch('https://api.lemonsqueezy.com/v1/licenses/activate', {{
            method: 'POST',
            headers: {{ 'Accept':'application/json','Content-Type':'application/json' }},
            body: JSON.stringify({{ license_key: key, instance_name: 'seller-tools-pro' }})
        }});
        var d = await r.json();
        if(d.activated) {{ localStorage.setItem('is_premium_user','true'); el.innerText='License activated! PRO unlocked.'; el.className='text-xs text-green-600 mt-1'; setTimeout(closePaywallModal,1500); }}
        else {{ el.innerText='Invalid license key.'; el.className='text-xs text-red-500 mt-1'; }}
    }} catch(e) {{ el.innerText='Network error. Try again.'; el.className='text-xs text-red-500 mt-1'; }}
}}
calculateProfit();
</script>
</body>
</html>"""


def build_walmart_html(p, c, cat):
    """Walmart 计算器"""
    country = p["countries"][c]
    symbol = ccy(country)
    plat_name = p["name"]
    cat_lc = cat.lower()
    ref_rates = {"electronics": 0.08, "home-kitchen": 0.15, "clothing": 0.10}
    ref_rate = ref_rates.get(cat_lc, 0.10)
    ref_pct = int(ref_rate * 100)
    title = f"{plat_name} {country} {cat_label(cat)} Profit Calculator ({CURRENT_YEAR})"
    desc = f"Calculate your {plat_name} {country} marketplace profit for {cat_label(cat)}. Includes referral fees and fulfillment costs."
    keywords = f"{plat_name} {country} calculator, {cat_label(cat)} profit, marketplace fee {CURRENT_YEAR}"
    h1 = f"{plat_name} {country} Profit Calculator"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <meta name="keywords" content="{keywords}">
    <link rel="stylesheet" href="tailwind.css">
    <style>.blur-overlay{{backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)}}</style>
</head>
<body class="bg-gray-50 text-gray-800 font-sans antialiased">

<header class="bg-white border-b border-gray-200 sticky top-0 z-40 shadow-sm">
    <div class="max-w-5xl mx-auto px-4 py-4 flex justify-between items-center">
        <div class="flex items-center space-x-2">
            <span class="text-2xl">🏪</span>
            <span class="font-bold text-xl tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-yellow-500 to-orange-600">SellerTools Pro</span>
        </div>
        <div class="flex items-center space-x-4">
            <span class="text-xs text-green-600 bg-green-50 px-2.5 py-1 rounded-full font-medium">● {CURRENT_YEAR} Live Rates</span>
            <button onclick="showLicenseModal()" class="text-xs bg-gray-900 hover:bg-gray-800 text-white px-3 py-1.5 rounded-lg font-medium transition">Activate PRO</button>
        </div>
    </div>
</header>

<main class="max-w-5xl mx-auto px-4 py-10 grid grid-cols-1 md:grid-cols-3 gap-8">
    <section class="md:col-span-2 bg-white border border-gray-200 rounded-2xl p-6 shadow-sm">
        <h1 class="text-2xl font-bold text-gray-900 mb-6">{h1} <span class="text-blue-600 text-lg">({cat_label_cn(cat)})</span></h1>
        <div class="space-y-6">
            <div>
                <h2 class="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-3">1. Pricing</h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Selling Price ({symbol})</label>
                        <input type="number" id="sellingPrice" value="59.99" class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none transition">
                    </div>
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Product Cost ({symbol})</label>
                        <input type="number" id="productCost" value="25.00" class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none transition">
                    </div>
                </div>
            </div>
            <div>
                <h2 class="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-3">2. Fulfillment</h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Shipping Cost ({symbol})</label>
                        <input type="number" id="shippingCost" value="5.50" class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none transition">
                    </div>
                </div>
            </div>
            <button onclick="calculateProfit()" class="w-full bg-gradient-to-r from-yellow-500 to-orange-600 hover:from-yellow-600 hover:to-orange-700 text-white font-semibold py-3 px-4 rounded-xl shadow-md transition transform active:scale-95">Calculate Profit</button>
        </div>
    </section>

    <section class="bg-gray-900 text-white rounded-2xl p-6 shadow-xl flex flex-col justify-between relative overflow-hidden">
        <div>
            <h2 class="text-lg font-bold tracking-tight text-gray-300 mb-6">Financial Summary</h2>
            <div class="space-y-4">
                <div class="flex justify-between border-b border-gray-800 pb-2">
                    <span class="text-gray-400">Referral Fee ({ref_pct}%)</span>
                    <span id="refFeeDisplay" class="font-medium">{symbol}0.00</span>
                </div>
                <div class="flex justify-between border-b border-gray-800 pb-2">
                    <span class="text-gray-400">Total Expenses</span>
                    <span id="totalExpensesDisplay" class="font-medium">{symbol}0.00</span>
                </div>
                <div class="flex justify-between pt-2">
                    <span class="text-gray-200 font-semibold text-lg">Net Profit</span>
                    <span id="netProfitDisplay" class="text-2xl font-bold text-green-400">{symbol}0.00</span>
                </div>
                <div class="flex justify-between">
                    <span class="text-gray-400">Net Margin</span>
                    <span id="marginDisplay" class="font-medium text-green-400">0.00%</span>
                </div>
            </div>
        </div>
        <div class="mt-8 pt-6 border-t border-gray-800">
            <button onclick="triggerPaywallAction()" class="w-full bg-yellow-500 hover:bg-yellow-400 text-gray-950 font-bold py-3 px-4 rounded-xl flex items-center justify-center space-x-2 transition shadow-lg">
                <span>📊</span>
                <span>Export Premium PDF Report</span>
            </button>
            <p class="text-center text-xs text-gray-500 mt-2">🔒 Pro feature. Requires activation key.</p>
        </div>
    </section>
</main>

<div id="paywallModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 bg-gray-950 bg-opacity-60 blur-overlay">
    <div class="bg-white rounded-2xl max-w-md w-full p-6 shadow-2xl relative border border-gray-100 text-gray-800">
        <button onclick="closePaywallModal()" class="absolute top-4 right-4 text-gray-400 hover:text-gray-600 text-xl" style="background:none;border:none;cursor:pointer;">&times;</button>
        <div class="text-center mb-6">
            <span class="text-4xl">💎</span>
            <h3 class="text-xl font-bold text-gray-900 mt-2">Unlock Premium</h3>
            <p class="text-sm text-gray-500 mt-1">Export professional PDF reports.</p>
        </div>
        <div class="bg-gray-50 rounded-xl p-4 mb-6 border border-gray-200">
            <div class="flex justify-between items-center">
                <div><p class="font-semibold text-gray-900">Lifetime Access</p><p class="text-xs text-gray-500">All calculators included.</p></div>
                <p class="text-2xl font-black text-gray-900">$4.99</p>
            </div>
            <a href="https://piwatools.lemonsqueezy.com/checkout/buy/95fff32f-9512-4004-9086-886f84ffadcb" target="_blank" class="block text-center bg-green-600 hover:bg-green-700 text-white font-semibold py-2.5 px-4 rounded-lg mt-4 transition shadow-sm">Buy License Key</a>
        </div>
        <div class="space-y-2">
            <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider">License Key</label>
            <div class="flex space-x-2">
                <input type="text" id="licenseKeyInput" placeholder="LK-XXXX-XXXX" class="flex-1 border border-gray-300 rounded-lg px-3 py-2 text-sm uppercase outline-none focus:ring-2 focus:ring-orange-500">
                <button onclick="verifyLicenseKey()" class="bg-gray-900 hover:bg-gray-800 text-white font-medium px-4 py-2 rounded-lg text-sm transition">Activate</button>
            </div>
            <p id="verifyMessage" class="text-xs mt-1"></p>
        </div>
    </div>
</div>

<script>
var CS = "{symbol}";
var REF_RATE = {ref_rate};

function calculateProfit() {{
    var price = parseFloat(document.getElementById('sellingPrice').value) || 0;
    var cost = parseFloat(document.getElementById('productCost').value) || 0;
    var shipping = parseFloat(document.getElementById('shippingCost').value) || 0;
    var refFee = price * REF_RATE;
    var totalExp = cost + shipping + refFee;
    var profit = price - totalExp;
    var margin = price > 0 ? (profit / price) * 100 : 0;
    document.getElementById('refFeeDisplay').innerText = CS + refFee.toFixed(2);
    document.getElementById('totalExpensesDisplay').innerText = CS + totalExp.toFixed(2);
    document.getElementById('netProfitDisplay').innerText = CS + profit.toFixed(2);
    document.getElementById('marginDisplay').innerText = margin.toFixed(2) + '%';
    document.getElementById('netProfitDisplay').className = profit >= 0 ? 'text-2xl font-bold text-green-400' : 'text-2xl font-bold text-red-400';
}}
function triggerPaywallAction() {{ var p = localStorage.getItem('is_premium_user') === 'true'; if(p) {{ alert('Generating premium PDF report... (Demo)'); }} else {{ showLicenseModal(); }} }}
function showLicenseModal() {{ document.getElementById('paywallModal').classList.remove('hidden'); }}
function closePaywallModal() {{ document.getElementById('paywallModal').classList.add('hidden'); }}
async function verifyLicenseKey() {{
    var key = document.getElementById('licenseKeyInput').value.trim();
    var el = document.getElementById('verifyMessage');
    if(!key) {{ el.innerText='Please enter a key.'; el.className='text-xs text-red-500 mt-1'; return; }}
    el.innerText='Verifying...'; el.className='text-xs text-yellow-600 mt-1';
    try {{
        var r = await fetch('https://api.lemonsqueezy.com/v1/licenses/activate', {{
            method: 'POST',
            headers: {{ 'Accept':'application/json','Content-Type':'application/json' }},
            body: JSON.stringify({{ license_key: key, instance_name: 'seller-tools-pro' }})
        }});
        var d = await r.json();
        if(d.activated) {{ localStorage.setItem('is_premium_user','true'); el.innerText='License activated! PRO unlocked.'; el.className='text-xs text-green-600 mt-1'; setTimeout(closePaywallModal,1500); }}
        else {{ el.innerText='Invalid license key.'; el.className='text-xs text-red-500 mt-1'; }}
    }} catch(e) {{ el.innerText='Network error. Try again.'; el.className='text-xs text-red-500 mt-1'; }}
}}
calculateProfit();
</script>
</body>
</html>"""


def build_mercadolibre_html(p, c, cat):
    """Mercado Libre 计算器"""
    country = p["countries"][c]
    symbol = ccy(country)
    plat_name = p["name"]
    # Mercado Libre commission: ~10-17% depending on category
    comm_rate = 0.13
    title = f"{plat_name} {country} {cat_label(cat)} Profit Calculator ({CURRENT_YEAR})"
    desc = f"Calculate your {plat_name} {country} selling profit for {cat_label(cat)}. Includes platform commission, VAT, and shipping costs."
    keywords = f"{plat_name} {country} calculator, {cat_label(cat)} profit, commission {CURRENT_YEAR}"
    h1 = f"{plat_name} {country} Profit Calculator"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <meta name="keywords" content="{keywords}">
    <link rel="stylesheet" href="tailwind.css">
    <style>.blur-overlay{{backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)}}</style>
</head>
<body class="bg-gray-50 text-gray-800 font-sans antialiased">

<header class="bg-white border-b border-gray-200 sticky top-0 z-40 shadow-sm">
    <div class="max-w-5xl mx-auto px-4 py-4 flex justify-between items-center">
        <div class="flex items-center space-x-2">
            <span class="text-2xl">🌎</span>
            <span class="font-bold text-xl tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-yellow-500 to-orange-600">SellerTools Pro</span>
        </div>
        <div class="flex items-center space-x-4">
            <span class="text-xs text-green-600 bg-green-50 px-2.5 py-1 rounded-full font-medium">● {CURRENT_YEAR} Live Rates</span>
            <button onclick="showLicenseModal()" class="text-xs bg-gray-900 hover:bg-gray-800 text-white px-3 py-1.5 rounded-lg font-medium transition">Activate PRO</button>
        </div>
    </div>
</header>

<main class="max-w-5xl mx-auto px-4 py-10 grid grid-cols-1 md:grid-cols-3 gap-8">
    <section class="md:col-span-2 bg-white border border-gray-200 rounded-2xl p-6 shadow-sm">
        <h1 class="text-2xl font-bold text-gray-900 mb-6">{h1} <span class="text-yellow-600 text-lg">({cat_label_cn(cat)})</span></h1>
        <div class="space-y-6">
            <div>
                <h2 class="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-3">1. Sale Details</h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Selling Price ({symbol})</label>
                        <input type="number" id="sellingPrice" value="499.99" class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none transition">
                    </div>
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Product Cost ({symbol})</label>
                        <input type="number" id="productCost" value="200.00" class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none transition">
                    </div>
                </div>
            </div>
            <div>
                <h2 class="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-3">2. Costs</h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Shipping Cost ({symbol})</label>
                        <input type="number" id="shippingCost" value="35.00" class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none transition">
                    </div>
                </div>
            </div>
            <button onclick="calculateProfit()" class="w-full bg-gradient-to-r from-yellow-500 to-orange-600 hover:from-yellow-600 hover:to-orange-700 text-white font-semibold py-3 px-4 rounded-xl shadow-md transition transform active:scale-95">Calculate Profit</button>
        </div>
    </section>

    <section class="bg-gray-900 text-white rounded-2xl p-6 shadow-xl flex flex-col justify-between relative overflow-hidden">
        <div>
            <h2 class="text-lg font-bold tracking-tight text-gray-300 mb-6">Financial Summary</h2>
            <div class="space-y-4">
                <div class="flex justify-between border-b border-gray-800 pb-2">
                    <span class="text-gray-400">Commission (13%)</span>
                    <span id="commFeeDisplay" class="font-medium">{symbol}0.00</span>
                </div>
                <div class="flex justify-between border-b border-gray-800 pb-2">
                    <span class="text-gray-400">Total Expenses</span>
                    <span id="totalExpensesDisplay" class="font-medium">{symbol}0.00</span>
                </div>
                <div class="flex justify-between pt-2">
                    <span class="text-gray-200 font-semibold text-lg">Net Profit</span>
                    <span id="netProfitDisplay" class="text-2xl font-bold text-green-400">{symbol}0.00</span>
                </div>
                <div class="flex justify-between">
                    <span class="text-gray-400">Net Margin</span>
                    <span id="marginDisplay" class="font-medium text-green-400">0.00%</span>
                </div>
            </div>
        </div>
        <div class="mt-8 pt-6 border-t border-gray-800">
            <button onclick="triggerPaywallAction()" class="w-full bg-yellow-500 hover:bg-yellow-400 text-gray-950 font-bold py-3 px-4 rounded-xl flex items-center justify-center space-x-2 transition shadow-lg">
                <span>📊</span>
                <span>Export Premium PDF Report</span>
            </button>
            <p class="text-center text-xs text-gray-500 mt-2">🔒 Pro feature. Requires activation key.</p>
        </div>
    </section>
</main>

<div id="paywallModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 bg-gray-950 bg-opacity-60 blur-overlay">
    <div class="bg-white rounded-2xl max-w-md w-full p-6 shadow-2xl relative border border-gray-100 text-gray-800">
        <button onclick="closePaywallModal()" class="absolute top-4 right-4 text-gray-400 hover:text-gray-600 text-xl" style="background:none;border:none;cursor:pointer;">&times;</button>
        <div class="text-center mb-6">
            <span class="text-4xl">💎</span>
            <h3 class="text-xl font-bold text-gray-900 mt-2">Unlock Premium</h3>
            <p class="text-sm text-gray-500 mt-1">Export professional PDF reports.</p>
        </div>
        <div class="bg-gray-50 rounded-xl p-4 mb-6 border border-gray-200">
            <div class="flex justify-between items-center">
                <div><p class="font-semibold text-gray-900">Lifetime Access</p><p class="text-xs text-gray-500">All calculators included.</p></div>
                <p class="text-2xl font-black text-gray-900">$4.99</p>
            </div>
            <a href="https://piwatools.lemonsqueezy.com/checkout/buy/95fff32f-9512-4004-9086-886f84ffadcb" target="_blank" class="block text-center bg-green-600 hover:bg-green-700 text-white font-semibold py-2.5 px-4 rounded-lg mt-4 transition shadow-sm">Buy License Key</a>
        </div>
        <div class="space-y-2">
            <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider">License Key</label>
            <div class="flex space-x-2">
                <input type="text" id="licenseKeyInput" placeholder="LK-XXXX-XXXX" class="flex-1 border border-gray-300 rounded-lg px-3 py-2 text-sm uppercase outline-none focus:ring-2 focus:ring-orange-500">
                <button onclick="verifyLicenseKey()" class="bg-gray-900 hover:bg-gray-800 text-white font-medium px-4 py-2 rounded-lg text-sm transition">Activate</button>
            </div>
            <p id="verifyMessage" class="text-xs mt-1"></p>
        </div>
    </div>
</div>

<script>
var CS = "{symbol}";

function calculateProfit() {{
    var price = parseFloat(document.getElementById('sellingPrice').value) || 0;
    var cost = parseFloat(document.getElementById('productCost').value) || 0;
    var shipping = parseFloat(document.getElementById('shippingCost').value) || 0;
    var comm = price * {comm_rate};
    var totalExp = cost + shipping + comm;
    var profit = price - totalExp;
    var margin = price > 0 ? (profit / price) * 100 : 0;
    document.getElementById('commFeeDisplay').innerText = CS + comm.toFixed(2);
    document.getElementById('totalExpensesDisplay').innerText = CS + totalExp.toFixed(2);
    document.getElementById('netProfitDisplay').innerText = CS + profit.toFixed(2);
    document.getElementById('marginDisplay').innerText = margin.toFixed(2) + '%';
    document.getElementById('netProfitDisplay').className = profit >= 0 ? 'text-2xl font-bold text-green-400' : 'text-2xl font-bold text-red-400';
}}
function triggerPaywallAction() {{ var p = localStorage.getItem('is_premium_user') === 'true'; if(p) {{ alert('Generating premium PDF report... (Demo)'); }} else {{ showLicenseModal(); }} }}
function showLicenseModal() {{ document.getElementById('paywallModal').classList.remove('hidden'); }}
function closePaywallModal() {{ document.getElementById('paywallModal').classList.add('hidden'); }}
async function verifyLicenseKey() {{
    var key = document.getElementById('licenseKeyInput').value.trim();
    var el = document.getElementById('verifyMessage');
    if(!key) {{ el.innerText='Please enter a key.'; el.className='text-xs text-red-500 mt-1'; return; }}
    el.innerText='Verifying...'; el.className='text-xs text-yellow-600 mt-1';
    try {{
        var r = await fetch('https://api.lemonsqueezy.com/v1/licenses/activate', {{
            method: 'POST',
            headers: {{ 'Accept':'application/json','Content-Type':'application/json' }},
            body: JSON.stringify({{ license_key: key, instance_name: 'seller-tools-pro' }})
        }});
        var d = await r.json();
        if(d.activated) {{ localStorage.setItem('is_premium_user','true'); el.innerText='License activated! PRO unlocked.'; el.className='text-xs text-green-600 mt-1'; setTimeout(closePaywallModal,1500); }}
        else {{ el.innerText='Invalid license key.'; el.className='text-xs text-red-500 mt-1'; }}
    }} catch(e) {{ el.innerText='Network error. Try again.'; el.className='text-xs text-red-500 mt-1'; }}
}}
calculateProfit();
</script>
</body>
</html>"""


# ============================================================
#  按平台类型映射到对应生成函数
# ============================================================
BUILDERS = {
    "amazon": build_amazon_html,
    "tiktok": build_tiktok_html,
    "shopify": build_shopify_html,
    "etsy": build_etsy_html,
    "ebay": build_ebay_html,
    "walmart": build_walmart_html,
    "mercadolibre": build_mercadolibre_html,
}

# ============================================================
#  主逻辑
# ============================================================

# 已有的页面不要重复生成
EXISTING = set()
for f in os.listdir("."):
    if f.endswith("-calculator.html") and f != "amazon-us-electronics-calculator.html":
        EXISTING.add(f)

OUT_DIR = "."

if __name__ == "__main__":
    total = 0
    skipped = 0

    print("=" * 55)
    print("  [跨境电商工具站] 批量生成计算器页面")
    print("  Platforms: Amazon / TikTok Shop / Shopify / Etsy / eBay / Walmart / Mercado Libre")
    print("=" * 55)

    for plat in PLATFORMS:
        builder = BUILDERS.get(plat["fee_type"])
        if not builder:
            continue

        for ci, country in enumerate(plat["countries"]):
            for cat in plat["categories"]:
                # Skip Amazon US Electronics — already exists as seed
                if plat["id"] == "amazon" and country == "US" and cat == "Electronics":
                    skipped += 1
                    continue

                filename = f"{plat['id']}-{country.lower()}-{cat.lower()}-calculator.html"

                if filename in EXISTING:
                    skipped += 1
                    continue

                html = builder(plat, ci, cat)
                filepath = os.path.join(OUT_DIR, filename)
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(html)
                print(f"  [生成] {filename}")
                total += 1

    # ============================================================
    #  3. 自动生成 index.html（包含所有工具卡片）
    # ============================================================
    print("")
    print("  [首页] 正在更新 index.html ...")

    all_tools = []

    def add_tool(pid, country_code, cat, link):
        """Add a tool card entry"""
        plat_info = [p for p in PLATFORMS if p["id"] == pid]
        if not plat_info:
            return
        p = plat_info[0]
        label = p["label"]
        country_name = country_code
        cat_name = cat_label(cat)
        cat_name_cn = cat_label_cn(cat)
        color = p["color"]

        tag_colors = {
            "orange": ("bg-orange-50", "text-orange-600"),
            "black": ("bg-black", "text-white"),
            "emerald": ("bg-emerald-50", "text-emerald-700"),
            "amber": ("bg-amber-50", "text-amber-600"),
            "blue": ("bg-blue-50", "text-blue-600"),
            "yellow": ("bg-yellow-50", "text-yellow-700"),
        }
        bg, tx = tag_colors.get(color, ("bg-gray-100", "text-gray-700"))

        tags = f"{label.lower()} {country_code.lower()} {cat.lower()}"

        # Description in English
        desc = f"Calculate {label} {country_code} {cat_name} profit, fees, and margin. {CURRENT_YEAR} rates."

        all_tools.append((pid, label, country_code, cat_name, cat_name_cn, bg, tx, tags, desc, link))

    # Add the seed tool
    add_tool("amazon", "US", "Electronics", "/amazon-us-electronics-calculator")

    # Add all generated tools
    for plat in PLATFORMS:
        for ci, country in enumerate(plat["countries"]):
            for cat in plat["categories"]:
                if plat["id"] == "amazon" and country == "US" and cat == "Electronics":
                    continue  # seed tool already added
                filename = f"{plat['id']}-{country.lower()}-{cat.lower()}-calculator.html"
                add_tool(plat["id"], country, cat, f"/{filename.replace('.html', '')}")

    # Build platform tab buttons
    platform_tabs = {}
    for pid, label, ccode, cname, cname_cn, bg, tx, tags, desc, link in all_tools:
        if pid not in platform_tabs:
            platform_tabs[pid] = label
    tab_keys = list(platform_tabs.keys())
    tab_order = ["amazon", "tiktok", "shopify", "etsy", "ebay", "walmart", "mercadolibre"]

    # Build index.html
    index_content = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>跨境电商工具站 - 卖家利润计算器大全 | SellerTools Pro</title>
    <meta name="description" content="免费的跨境电商工具集，涵盖亚马逊、TikTok Shop、Shopify、Etsy、eBay、Walmart、Mercado Libre等平台的FBA利润计算器、ROI计算器、佣金计算器，帮助跨境卖家精准算账。">
    <meta name="keywords" content="跨境电商工具, FBA利润计算器, 亚马逊计算器, 跨境卖家工具">
    <link rel="stylesheet" href="tailwind.css">
</head>
<body class="bg-gray-50 text-gray-800 font-sans antialiased">

    <header class="bg-white border-b border-gray-200 sticky top-0 z-40">
        <div class="max-w-6xl mx-auto px-4 py-4 flex justify-between items-center">
            <div class="flex items-center space-x-2">
                <span class="text-2xl">⚡</span>
                <span class="font-bold text-xl tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-yellow-500 to-orange-600">SellerTools Pro</span>
            </div>
            <a href="https://piwatools.lemonsqueezy.com/checkout/buy/95fff32f-9512-4004-9086-886f84ffadcb" target="_blank" class="text-sm bg-gray-900 hover:bg-gray-800 text-white px-4 py-2 rounded-lg font-medium transition">Activate Pro</a>
        </div>
    </header>

    <section class="bg-gray-950 text-white py-20 px-4 text-center relative overflow-hidden">
        <div class="max-w-4xl mx-auto relative">
            <span class="text-sm bg-yellow-500/20 text-yellow-400 border border-yellow-500/30 px-3 py-1 rounded-full font-semibold">\U0001f525 Cross-Border Seller Tools</span>
            <h1 class="text-4xl sm:text-5xl font-black tracking-tight mt-6 mb-4 text-transparent bg-clip-text bg-gradient-to-r from-yellow-400 via-orange-400 to-yellow-200">
                """ + str(len(all_tools)) + """+ Free Seller Calculators
            </h1>
            <p class="text-gray-400 text-lg max-w-2xl mx-auto leading-relaxed">
                Real-time profit, margin, ROI &amp; commission calculators for Amazon, TikTok Shop, Shopify, Etsy, eBay, Walmart, Mercado Libre &amp; more.<br>
                Updated for """ + CURRENT_YEAR + """. No registration required.
            </p>
        </div>
    </section>

    <div class="max-w-6xl mx-auto px-4 -mt-8 mb-8">
        <div class="bg-white rounded-2xl shadow-sm border border-gray-200 p-2 flex flex-wrap justify-center gap-2">
            <button onclick="filterTools('all')" class="tab-btn px-5 py-2.5 rounded-xl text-sm font-medium transition bg-gray-900 text-white" data-tab="all">All Tools</button>
"""
    for key in tab_order:
        if key in platform_tabs:
            label = platform_tabs[key]
            index_content += f'            <button onclick="filterTools(\'{key}\')" class="tab-btn px-5 py-2.5 rounded-xl text-sm font-medium transition bg-gray-50 text-gray-600 hover:bg-gray-100" data-tab="{key}">{label}</button>\n'

    index_content += """        </div>
    </div>

    <div class="max-w-6xl mx-auto px-4 mb-8">
        <input type="text" id="searchInput" oninput="filterTools(getCurrentTab())" placeholder="Search by platform, country, or category..."
               class="w-full bg-white border border-gray-200 rounded-xl px-5 py-3 shadow-sm focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500 transition placeholder:text-gray-400">
    </div>

    <main class="max-w-6xl mx-auto px-4 pb-20">
        <div id="toolsGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
"""

    for pid, label, ccode, cname, cname_cn, bg, tx, tags, desc, link in all_tools:
        plat_label = f"{label} {ccode}"
        index_content += f"""            <div class="tool-card bg-white border border-gray-200 rounded-2xl p-6 shadow-sm hover:shadow-lg transition flex flex-col justify-between" data-platform="{pid}" data-tags="{tags}">
                <div>
                    <div class="flex justify-between items-start mb-3">
                        <span class="text-xs {bg} {tx} px-2.5 py-1 rounded-md font-semibold">{plat_label}</span>
                        <span class="text-xs text-gray-400">Profit Calc</span>
                    </div>
                    <h3 class="text-lg font-bold text-gray-900 mb-2">{cname}</h3>
                    <p class="text-sm text-gray-500 mb-4">{desc}</p>
                </div>
                <a href="{link}" class="block text-center bg-gray-900 hover:bg-gray-800 text-white font-medium py-2.5 px-4 rounded-xl text-sm transition">Launch Tool →</a>
            </div>
"""

    index_content += """        </div>
        <div id="noResults" class="hidden text-center py-20">
            <span class="text-5xl">\U0001f50d</span>
            <p class="text-gray-500 mt-4 text-lg">No matching tools found</p>
            <p class="text-gray-400 text-sm mt-1">Try a different keyword or platform filter</p>
        </div>
    </main>

    <section class="bg-white border-t border-gray-200 py-20 px-4">
        <div class="max-w-6xl mx-auto">
            <h2 class="text-2xl font-bold text-center text-gray-900 mb-4">Why SellerTools Pro?</h2>
            <p class="text-gray-500 text-center mb-12 max-w-2xl mx-auto">Free tools for cross-border sellers. Updated for """ + CURRENT_YEAR + """ rates.</p>
            <div class="grid grid-cols-1 md:grid-cols-4 gap-8 text-center">
                <div>
                    <span class="text-4xl">⚡</span>
                    <h3 class="font-bold text-gray-900 mt-3 mb-2">Real-time</h3>
                    <p class="text-sm text-gray-500">All calculations run in your browser. Instant results.</p>
                </div>
                <div>
                    <span class="text-4xl">\U0001f512</span>
                    <h3 class="font-bold text-gray-900 mt-3 mb-2">Private</h3>
                    <p class="text-sm text-gray-500">Data stays on your device. Nothing uploaded.</p>
                </div>
                <div>
                    <span class="text-4xl">\U0001f30d</span>
                    <h3 class="font-bold text-gray-900 mt-3 mb-2">Multi-Platform</h3>
                    <p class="text-sm text-gray-500">Amazon, TikTok Shop, Shopify, Etsy, eBay &amp; more.</p>
                </div>
                <div>
                    <span class="text-4xl">\U0001f4b0</span>
                    <h3 class="font-bold text-gray-900 mt-3 mb-2">Free</h3>
                    <p class="text-sm text-gray-500">Basic features free. Premium unlocks PDF exports.</p>
                </div>
            </div>
        </div>
    </section>

    <footer class="bg-gray-950 text-gray-500 py-12 px-4 text-center text-sm">
        <p>© """ + CURRENT_YEAR + """ SellerTools Pro. All rights reserved.</p>
        <p class="mt-2 text-xs text-gray-600">Cross-border seller tools network</p>
    </footer>

    <script>
        var currentTab = 'all';
        function getCurrentTab() { return currentTab; }
        function filterTools(platform) {
            currentTab = platform;
            var query = document.getElementById('searchInput').value.toLowerCase().trim();
            document.querySelectorAll('.tab-btn').forEach(function(btn) {
                if (btn.dataset.tab === platform || (platform === 'all' && btn.dataset.tab === 'all')) {
                    btn.className = "tab-btn px-5 py-2.5 rounded-xl text-sm font-medium transition bg-gray-900 text-white";
                } else {
                    btn.className = "tab-btn px-5 py-2.5 rounded-xl text-sm font-medium transition bg-gray-50 text-gray-600 hover:bg-gray-100";
                }
            });
            var cards = document.querySelectorAll('.tool-card');
            var count = 0;
            cards.forEach(function(card) {
                var matchTab = (platform === 'all' || card.dataset.platform === platform);
                var matchSearch = !query || card.dataset.tags.includes(query);
                if (matchTab && matchSearch) {
                    card.classList.remove('hidden');
                    card.style.display = 'flex';
                    count++;
                } else {
                    card.classList.add('hidden');
                }
            });
            document.getElementById('noResults').classList.toggle('hidden', count > 0);
        }
    </script>
</body>
</html>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_content)

    print(f"  [首页] index.html 已更新 — 包含 {len(all_tools)} 个工具卡片")
    print("=" * 55)
    print(f"  DONE! 全站共 {len(all_tools)} 个计算器页面")
    print("=" * 55)
    print("")
    print("  接下来把代码推送到 GitHub 即可自动部署到线上：")
    print("    git add .")
    print('    git commit -m "add bulk-generated calculator tools"')
    print("    git push")
