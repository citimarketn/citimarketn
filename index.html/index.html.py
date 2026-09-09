<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>سوق السويس الإلكتروني - منصة تجار محافظة السويس</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;800;900&display=swap');
        * { font-family: 'Cairo', sans-serif; }
        body { background-color: #f7f5f0; color: #1c1917; }

        :root {
            --brand-deep: #0b3d3a;
            --brand-mid: #0f5c56;
            --brand-gold: #d4a537;
            --brand-gold-light: #e8c565;
        }
        .bg-brand-deep { background-color: var(--brand-deep); }
        .bg-brand-mid { background-color: var(--brand-mid); }
        .text-brand-gold { color: var(--brand-gold); }
        .bg-brand-gold { background-color: var(--brand-gold); }
        .border-brand-gold { border-color: var(--brand-gold); }

        .hero-pattern {
            background-image: radial-gradient(circle at 20% 20%, rgba(212,165,55,0.12) 0%, transparent 40%),
                              radial-gradient(circle at 80% 60%, rgba(11,61,58,0.15) 0%, transparent 45%);
        }
        .card-hover { transition: transform .25s ease, box-shadow .25s ease; }
        .card-hover:hover { transform: translateY(-4px); box-shadow: 0 12px 30px -8px rgba(11,61,58,0.18); }

        ::-webkit-scrollbar { width: 8px; height: 8px; }
        ::-webkit-scrollbar-thumb { background: #cbd5c9; border-radius: 10px; }
    </style>
</head>
<body class="min-h-screen flex flex-col">

    <!-- Global Header -->
    <header class="bg-brand-deep text-white shadow-lg sticky top-0 z-50">
        <div class="container mx-auto px-4 py-3 flex flex-wrap justify-between items-center">
            <div class="flex items-center space-x-3 space-x-reverse cursor-pointer" onclick="showHome()">
                <div class="bg-brand-gold text-brand-deep p-2.5 rounded-xl font-black text-xl flex items-center justify-center shadow-md">
                    <i class="fa-solid fa-store"></i>
                </div>
                <div>
                    <h1 class="text-lg font-black tracking-wide">سوق السويس الإلكتروني</h1>
                    <p class="text-[11px] text-emerald-200/70">بإشراف شركة سوق المدينة للتسويق</p>
                </div>
            </div>

            <div class="flex items-center space-x-3 space-x-reverse mt-2 sm:mt-0">
                <a href="https://wa.me/201118872502?text=أرغب%20في%20الانضمام%20كتاجر%20في%20سوق%20السويس" target="_blank" class="bg-emerald-600 hover:bg-emerald-500 text-white px-4 py-2 rounded-xl text-sm font-bold transition flex items-center gap-2 shadow">
                    <span>انضم كتاجر</span>
                    <i class="fa-brands fa-whatsapp text-lg"></i>
                </a>
                <button onclick="openAuthModal('login')" class="bg-white/10 hover:bg-white/20 text-white border border-white/20 px-4 py-2 rounded-xl text-sm font-bold transition flex items-center gap-2 shadow backdrop-blur-sm">
                    <span>حساب العملاء</span>
                    <i class="fa-solid fa-user text-brand-gold"></i>
                </button>
            </div>
        </div>
    </header>

    <!-- MAIN CONTAINER -->
    <main class="flex-grow">

        <!-- ================= VIEW 1: HOME PAGE ================= -->
        <div id="view-home">
            <!-- Hero Section -->
            <section class="hero-pattern bg-gradient-to-br from-[#0b3d3a] via-[#0f5c56] to-[#0b3d3a] text-white py-20 px-4 text-center relative overflow-hidden">
                <div class="container mx-auto max-w-4xl relative z-10">
                    <span class="inline-block bg-white/10 border border-white/20 text-brand-gold text-xs font-bold px-4 py-1.5 rounded-full mb-5 backdrop-blur-sm">
                        <i class="fa-solid fa-location-dot ml-1"></i> محافظة السويس - حي الأربعين وباقي الاحياء
                    </span>
                    <h2 class="text-3xl sm:text-5xl font-black mb-6 leading-tight">دليل محلات وأنشطة السويس الرقمي</h2>
                    <p class="text-lg sm:text-xl text-emerald-50/90 mb-4 leading-relaxed">تصفح مئات المتاجر والسلع والخدمات في السويس واطلبها فوراً عبر الواتساب.</p>

                    <div class="bg-white p-2 rounded-2xl shadow-2xl flex flex-col sm:flex-row gap-2 max-w-2xl mx-auto">
                        <div class="flex-grow flex items-center px-3 py-2 bg-slate-100 rounded-xl">
                            <i class="fa-solid fa-search text-slate-400 ml-2"></i>
                            <input type="text" id="main-search" oninput="secureSearchInput(this)" placeholder="ابحث عن محل، منتج، خدمة، أو سلعة..." class="bg-transparent w-full focus:outline-none text-slate-800 text-sm">
                        </div>
                        <button onclick="secureAction('search', () => { alert('تم تحديث نتائج البحث الآمن'); })" class="bg-brand-gold hover:bg-brand-gold-light text-brand-deep px-6 py-3 rounded-xl font-bold transition shadow">بحث ذكي</button>
                    </div>

                    <div class="flex flex-wrap justify-center gap-6 mt-10 text-emerald-50/80 text-xs sm:text-sm">
                        <div class="flex items-center gap-2"><i class="fa-solid fa-shop text-brand-gold"></i> 50 متجراً معتمداً</div>
                        <div class="flex items-center gap-2"><i class="fa-brands fa-whatsapp text-brand-gold"></i> تواصل مباشر بالواتساب</div>
                        <div class="flex items-center gap-2"><i class="fa-solid fa-shield-halved text-brand-gold"></i> حماية تامة للبيانات</div>
                    </div>
                </div>
            </section>

            <!-- Categories Section -->
            <section class="container mx-auto px-4 py-14">
                <div class="text-center mb-10">
                    <h3 class="text-2xl font-black text-slate-900 mb-2">أقسام السوق الرئيسية</h3>
                    <p class="text-slate-600 text-sm">اختر القسم لتصفح المتاجر والمنتجات المتخصصة</p>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6" id="categories-grid">
                    <!-- تتولد الأقسام ديناميكياً عبر JavaScript -->
                </div>
            </section>

            <!-- Shipping & Delivery Partners -->
            <section class="bg-slate-50 border-y border-slate-100 py-14 px-4">
                <div class="container mx-auto">
                    <div class="text-center mb-10">
                        <h3 class="text-2xl font-black text-slate-900 mb-2">شركات الشحن والتوصيل في السويس</h3>
                        <p class="text-slate-600 text-sm">شركاؤنا لضمان توصيل طلباتك حتى باب المنزل بسرعة وأمان</p>
                    </div>
                    <div id="shipping-grid" class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-4">
                        <!-- تتولد شركات الشحن ديناميكيًا -->
                    </div>
                </div>
            </section>

            <!-- Shops Section (50 Shops) -->
            <section id="shops-section" class="container mx-auto px-4 py-12">
                <div class="flex flex-col md:flex-row justify-between items-center mb-8 gap-4 border-b border-slate-200 pb-4">
                    <h3 class="text-2xl font-black text-slate-900">دليل المتاجر والأنشطة (50 متجراً)</h3>
                </div>

                <div id="shops-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                    <!-- تتولد المحلات هنا ديناميكيًا -->
                </div>
            </section>

            <!-- Subscriptions & Footer Info Links -->
            <section class="bg-slate-100 py-16 px-4 border-t border-slate-200">
                <div class="container mx-auto max-w-4xl text-center">
                    <h3 class="text-2xl sm:text-3xl font-black text-slate-900 mb-2">باقات الاشتراك والاشتراكات الشهرية</h3>
                    <p class="text-slate-600 text-sm mb-10">نظام اشتراكات وباقات إعلانية واضحة بدون عمولة على مبيعاتك</p>

                    <div class="grid grid-cols-1 md:grid-cols-3 gap-5 max-w-3xl mx-auto mb-10">
                        <div class="card-hover bg-white p-6 rounded-3xl shadow-sm border border-slate-200 flex flex-col justify-between">
                            <div>
                                <h4 class="text-lg font-bold text-slate-900 mb-1">باقة 6 أشهر</h4>
                                <div class="text-2xl font-black text-slate-900 my-3">2700 <span class="text-xs font-normal text-slate-500">ج.م</span></div>
                            </div>
                            <a href="https://wa.me/201118872502?text=أرغب%20في%20الاشتراك%20بباقة%206%20أشهر" target="_blank" class="bg-brand-deep hover:bg-emerald-700 text-white py-2.5 rounded-xl font-bold text-xs transition block text-center">اشترك الآن</a>
                        </div>
                        <div class="card-hover bg-white p-6 rounded-3xl shadow-sm border-2 border-brand-gold flex flex-col justify-between relative">
                            <span class="absolute -top-3 right-1/2 transform translate-x-1/2 bg-brand-gold text-brand-deep text-xs font-bold px-3 py-0.5 rounded-full shadow">الأكثر طلباً</span>
                            <div>
                                <h4 class="text-lg font-bold text-slate-900 mb-1">باقة 3 أشهر</h4>
                                <div class="text-2xl font-black text-brand-gold my-3">1250 <span class="text-xs font-normal text-slate-500">ج.م</span></div>
                            </div>
                            <a href="https://wa.me/201118872502?text=أرغب%20في%20الاشتراك%20بباقة%203%20أشهر" target="_blank" class="bg-brand-gold hover:bg-brand-gold-light text-brand-deep py-2.5 rounded-xl font-bold text-xs transition block text-center">اشترك الآن</a>
                        </div>
                        <div class="card-hover bg-white p-6 rounded-3xl shadow-sm border border-slate-200 flex flex-col justify-between">
                            <div>
                                <h4 class="text-lg font-bold text-slate-900 mb-1">باقة الشهر</h4>
                                <div class="text-2xl font-black text-slate-900 my-3">500 <span class="text-xs font-normal text-slate-500">جنيه / شهرياً</span></div>
                            </div>
                            <a href="https://wa.me/201118872502?text=أرغب%20في%20الاشتراك%20بباقة%20الشهر" target="_blank" class="bg-brand-deep hover:bg-emerald-700 text-white py-2.5 rounded-xl font-bold text-xs transition block text-center">اشترك الآن</a>
                        </div>
                    </div>

                    <div class="flex flex-wrap justify-center gap-4 text-xs font-bold text-slate-600">
                        <button onclick="openInfoModal('about')" class="hover:text-brand-deep underline">عن المنصة</button>
                        <button onclick="openInfoModal('customerService')" class="hover:text-brand-deep underline">خدمة العملاء</button>
                        <button onclick="openInfoModal('support')" class="hover:text-brand-deep underline">الدعم الفني</button>
                        <button onclick="openInfoModal('returnPolicy')" class="hover:text-brand-deep underline">سياسة الاسترجاع</button>
                        <button onclick="openInfoModal('privacy')" class="hover:text-brand-deep underline">الخصوصية والأمان</button>
                        <button onclick="openInfoModal('terms')" class="hover:text-brand-deep underline">شروط الاستخدام</button>
                    </div>
                </div>
            </section>
        </div>

        <!-- ================= VIEW 2: SHOP INTERIOR ================= -->
        <div id="view-shop" class="hidden relative">
            <button onclick="showHome()" class="fixed bottom-5 left-5 z-40 bg-brand-deep hover:bg-brand-mid text-white w-12 h-12 rounded-full shadow-2xl flex items-center justify-center text-lg transition border-2 border-white" title="العودة للرئيسية">
                <i class="fa-solid fa-house"></i>
            </button>

            <section class="relative">
                <div id="shop-cover" class="min-h-[320px] w-full bg-gradient-to-br from-[#0b3d3a] via-[#0f5c56] to-[#0b3d3a] bg-cover bg-center relative overflow-hidden flex flex-col justify-end">
                    <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/40 to-black/10"></div>
                    
                    <button onclick="openMerchantPanel()" class="absolute top-4 right-4 w-11 h-11 bg-white/20 hover:bg-white/40 text-white rounded-full flex items-center justify-center shadow-lg z-20 backdrop-blur-md transition border border-white/30" title="لوحة تحكم التاجر">
                        <i class="fa-solid fa-lock text-sm text-brand-gold"></i>
                    </button>

                    <div class="relative z-10 px-4 sm:px-8 pb-8">
                        <div class="container mx-auto max-w-5xl flex items-end justify-between flex-wrap gap-4">
                            <div class="flex items-end gap-4 flex-wrap">
                                <div class="relative group">
                                    <div id="shop-logo" class="w-24 h-24 sm:w-28 sm:h-28 bg-white text-brand-deep rounded-3xl flex items-center justify-center text-3xl font-black shadow-2xl border-4 border-white bg-cover bg-center relative">
                                        <i id="shop-logo-icon" class="fa-solid fa-store"></i>
                                    </div>
                                    <button onclick="changeLogoImage()" class="absolute bottom-1 right-1 bg-brand-gold text-brand-deep w-7 h-7 rounded-full text-xs shadow hidden merchant-edit-ctrl items-center justify-center" title="تغيير الشعار"><i class="fa-solid fa-camera"></i></button>
                                </div>
                                <div class="text-right">
                                    <h2 id="display-shop-name" class="text-2xl sm:text-3xl font-black text-white mb-1 drop-shadow">اسم المتجر</h2>
                                    <p id="display-shop-cat" class="text-brand-gold font-bold text-xs sm:text-sm mb-3">التصنيف</p>
                                    <div id="display-shop-bio" class="text-xs text-emerald-100/90 max-w-md mb-2">نبذة تعريفية مختصرة عن المتجر والخدمات المقدمة لأهالي السويس.</div>
                                </div>
                            </div>
                            <div class="flex items-center gap-3">
                                <a id="shop-whatsapp-btn" href="#" target="_blank" class="inline-flex items-center gap-2 bg-emerald-600 hover:bg-emerald-500 text-white px-6 py-3 rounded-xl font-bold transition shadow-xl text-sm">
                                    <i class="fa-brands fa-whatsapp text-xl"></i> تواصل بالواتساب
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Shop Shelves & Products Content -->
            <section class="container mx-auto px-4 py-12 max-w-5xl">
                <!-- Shelves Section -->
                <div class="flex justify-between items-center mb-6">
                    <h3 class="text-2xl font-black text-slate-900"><i class="fa-solid fa-layer-group ml-2 text-brand-gold"></i> رفوف وعروض المتجر</h3>
                    <button onclick="addShelf()" class="bg-brand-deep text-white px-4 py-2 rounded-xl text-xs font-bold hidden merchant-edit-ctrl items-center gap-1 shadow"><i class="fa-solid fa-plus"></i> إضافة رف جديد</button>
                </div>
                <div id="shelves-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-2 gap-6 mb-14">
                    <!-- تتولد الرفوف ديناميكياً -->
                </div>

                <!-- Products Section -->
                <div class="flex justify-between items-center mb-6">
                    <h3 class="text-2xl font-black text-slate-900"><i class="fa-solid fa-box-open ml-2 text-brand-gold"></i> منتجات وخدمات المتجر</h3>
                    <button onclick="addProduct()" class="bg-brand-deep text-white px-4 py-2 rounded-xl text-xs font-bold hidden merchant-edit-ctrl items-center gap-1 shadow"><i class="fa-solid fa-plus"></i> إضافة منتج جديد</button>
                </div>
                <div id="products-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                    <!-- تتولد المنتجات ديناميكياً -->
                </div>
            </section>
        </div>
    </main>

    <!-- Global Footer -->
    <footer class="bg-brand-deep text-white pt-12 pb-6 px-4 mt-auto">
        <div class="container mx-auto max-w-6xl text-center text-sm text-emerald-50/80">
            <p>جميع الحقوق محفوظة © 2026 - سوق السويس الإلكتروني (تصميم شركة سوق المدينة للتسويق)</p>
        </div>
    </footer>

    <!-- MODALS -->

    <!-- Merchant Login Modal -->
    <div id="merchant-login-modal" class="fixed inset-0 bg-black/60 z-50 hidden flex items-center justify-center p-4 backdrop-blur-sm">
        <div class="bg-white rounded-3xl max-w-md w-full p-6 shadow-2xl relative">
            <button onclick="closeMerchantLoginModal()" class="absolute top-4 left-4 text-slate-400 hover:text-slate-600"><i class="fa-solid fa-xmark text-xl"></i></button>
            <div class="text-center mb-6">
                <div class="w-14 h-14 bg-brand-deep text-brand-gold rounded-2xl mx-auto flex items-center justify-center text-2xl mb-3 shadow"><i class="fa-solid fa-lock"></i></div>
                <h3 class="text-xl font-black text-slate-900">تسجيل دخول التاجر</h3>
                <p class="text-xs text-slate-500 mt-1">أدخل رقم الواتساب المسجل للمتجر لتفعيل وضع التعديل والإدارة</p>
            </div>
            <div class="space-y-4">
                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-1">رقم الواتساب المسجل</label>
                    <input type="text" id="merchant-whatsapp-input" placeholder="01118872502" class="w-full bg-slate-100 border border-slate-200 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-brand-gold">
                </div>
                <button onclick="submitMerchantLogin()" class="w-full bg-brand-deep hover:bg-brand-mid text-white py-3 rounded-xl font-bold text-sm shadow transition">تحقق ودخول الإدارة</button>
            </div>
        </div>
    </div>

    <!-- Customer Auth Modal -->
    <div id="auth-modal" class="fixed inset-0 bg-black/60 z-50 hidden flex items-center justify-center p-4 backdrop-blur-sm">
        <div class="bg-white rounded-3xl max-w-md w-full p-6 shadow-2xl relative">
            <button onclick="closeAuthModal()" class="absolute top-4 left-4 text-slate-400 hover:text-slate-600"><i class="fa-solid fa-xmark text-xl"></i></button>
            <div class="flex border-b border-slate-100 mb-6 pb-2">
                <button onclick="switchAuthTab('login')" id="tab-login-btn" class="flex-1 pb-2 font-bold text-brand-deep border-b-2 border-brand-deep text-sm">تسجيل الدخول</button>
                <button onclick="switchAuthTab('signup')" id="tab-signup-btn" class="flex-1 pb-2 font-bold text-slate-400 text-sm">حساب جديد</button>
            </div>
            
            <div id="auth-form-container">
                <!-- تتولد حقول الدخول/التسجيل هنا -->
            </div>
        </div>
    </div>

    <!-- Info Modal -->
    <div id="info-modal" class="fixed inset-0 bg-black/60 z-50 hidden flex items-center justify-center p-4 backdrop-blur-sm">
        <div class="bg-white rounded-3xl max-w-lg w-full p-6 shadow-2xl relative max-h-[80vh] overflow-y-auto">
            <button onclick="closeInfoModal()" class="absolute top-4 left-4 text-slate-400 hover:text-slate-600"><i class="fa-solid fa-xmark text-xl"></i></button>
            <h3 id="info-modal-title" class="text-xl font-black text-slate-900 mb-3">عنوان القائمة</h3>
            <div id="info-modal-body" class="text-xs sm:text-sm text-slate-600 leading-relaxed space-y-3"></div>
        </div>
    </div>

    <!-- SCRIPT LOGIC -->
    <script>
        // Global Variables
        let actionLocks = {};
        let currentShopName = "";
        let currentShopCat = "";
        let merchantEditMode = false;
        let shopDataCache = {};

        const shippingCompanies = [
            { name: 'بوسطة (Bosta)', icon: 'fa-truck-fast' },
            { name: 'سويس إكسبريس', icon: 'fa-truck' },
            { name: 'سويس دليفري', icon: 'fa-motorcycle' },
            { name: 'أرجنت شيب', icon: 'fa-box' },
            { name: 'فاملي شيف', icon: 'fa-van-shuttle' },
            { name: 'سرعة للتوصيل', icon: 'fa-shipping-fast' }
        ];

        const shopNames = [
            'المدينة للتجارة والتوكيلات', 'السويس للإلكترونيات الحديثة', 'عطور ومستحضرات النيل',
            'توكيلات الموبايلات والكمبيوتر', 'ملابس العائلة العصرية', 'عطارة التوابل الذهبية',
            'سوبر ماركت الخير والبركة', 'أثاث ومفروشات القنال', 'قطع غيار السيارات المتطورة',
            'مستلزمات منزلية وأدوات مطبخ', 'أجهزة كهربائية متكاملة', 'الأسماك الطازجة البحرية',
            'مكتبة وادوات مكتبية الطالب', 'حلواني ومخبوزات السويس', 'إكسسوارات الهواتف الذكية', 'مقاولات وصيانة عامة'
        ];

        const cats = [
            { id: 'cat-1', name: 'إلكترونيات وأجهزة كهربائية', icon: 'fa-laptop', desc: 'شاشات، هواتف، أجهزة منزلية، قطع غيار' },
            { id: 'cat-2', name: 'ملابس وموضة وأحذية', icon: 'fa-shirt', desc: 'أزياء رجالية، نسائية، أطفال، أحذية' },
            { id: 'cat-3', name: 'مواد غذائية وعطارة وأسماك', icon: 'fa-basket-shopping', desc: 'سلع تموينية، أسماك طازجة، عطارة' },
            { id: 'cat-4', name: 'أثاث وديكور ومفروشات', icon: 'fa-couch', desc: 'غرف نوم، مجالس، ديكورات، مفروشات' },
            { id: 'cat-5', name: 'خدمات ومستلزمات سيارات', icon: 'fa-car', desc: 'قطع غيار، زيوت، إكسسوارات سيارات' },
            { id: 'cat-6', name: 'خدمات عامة ومهنية', icon: 'fa-screwdriver-wrench', desc: 'سباكة، كهرباء، مقاولات، تنظيف صيانة' }
        ];

        const infoContent = {
            about: { title: 'عن سوق السويس الإلكتروني', text: 'منصة رقمية متكاملة تابعة لشركة سوق المدينة للتسويق، تهدف لربط تجار وأنشطة محافظة السويس بعملائهم مباشرة عبر الواتساب وبدون عمولات على المبيعات.' },
            customerService: { title: 'خدمة العملاء', text: 'فريق دعم فني متواجد طوال أيام الأسبوع لمساعدة أهالي السويس في إتمام عمليات الشراء والوصول للمتاجر بسرعة.' },
            support: { title: 'الدعم الفني للتجار', text: 'نقدم حلولاً تقنية متكاملة ومتابعة دورية لتحديث أسعار ومنتجات المتاجر المشاركة بكل سهولة.' },
            returnPolicy: { title: 'سياسة الاسترجاع', text: 'تخضع عمليات الاسترجاع والاستبدال للسياسة الخاصة بكل متجر معتمد داخل المنصة وفقاً لضوابط وحقوق المستهلك.' },
            privacy: { title: 'الخصوصية والأمان', text: 'نحافظ على سرية بياناتك الشخصية ولا نشاركها مع أي أطراف خارجية، مع تأمين كامل لبيانات التصفح.' },
            terms: { title: 'شروط الاستخدام', text: 'استخدامك للمنصة يقر بموافقتك على التواصل المباشر مع التجار عبر الواتساب وعدم استخدام المنصة لأي أغراض مخالفة للقانون.' }
        };

        // Core Security & Navigation Functions
        function secureSearchInput(inputElement) {
            inputElement.value = inputElement.value.replace(/[<>]/g, '');
        }

        function secureAction(actionId, callback) {
            if (actionLocks[actionId]) return;
            actionLocks[actionId] = true;
            setTimeout(() => { actionLocks[actionId] = false; }, 800);
            callback();
        }

        function saveSecureData(key, value) {
            try {
                const encoded = btoa(encodeURIComponent(JSON.stringify(value)));
                localStorage.setItem(key, encoded);
            } catch (e) {
                localStorage.setItem(key, JSON.stringify(value));
            }
        }

        function showHome() {
            document.getElementById('view-home').classList.remove('hidden');
            document.getElementById('view-shop').classList.add('hidden');
            merchantEditMode = false;
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        function openShop(name, cat) {
            currentShopName = name;
            currentShopCat = cat;
            merchantEditMode = false; // Security measure: reset edit mode on open
            document.getElementById('view-home').classList.add('hidden');
            document.getElementById('view-shop').classList.remove('hidden');
            
            document.getElementById('display-shop-name').innerText = name;
            document.getElementById('display-shop-cat').innerText = cat;
            document.getElementById('shop-whatsapp-btn').href = `https://wa.me/201118872502?text=مرحباً، أستفسر من ${name}`;
            
            applyShopBranding();
            renderShelvesForShop(name);
            renderProductsForShop(name);
            renderShopBio();
            toggleMerchantEditControls(false);
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        function toggleMerchantPanel() {
            openMerchantPanel();
        }

        // Authentication & Modal Functions
        function openAuthModal(mode) {
            document.getElementById('auth-modal').classList.remove('hidden');
            switchAuthTab(mode);
        }

        function closeAuthModal() {
            document.getElementById('auth-modal').classList.add('hidden');
        }

        function switchAuthTab(mode) {
            const loginBtn = document.getElementById('tab-login-btn');
            const signupBtn = document.getElementById('tab-signup-btn');
            const container = document.getElementById('auth-form-container');

            if (mode === 'login') {
                loginBtn.className = "flex-1 pb-2 font-bold text-brand-deep border-b-2 border-brand-deep text-sm";
                signupBtn.className = "flex-1 pb-2 font-bold text-slate-400 text-sm";
                container.innerHTML = `
                    <div class="space-y-4">
                        <div>
                            <label class="block text-xs font-bold text-slate-700 mb-1">رقم الهاتف المحمول</label>
                            <input type="text" placeholder="010xxxxxxxx" class="w-full bg-slate-100 border border-slate-200 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-brand-gold">
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-slate-700 mb-1">كلمة المرور</label>
                            <input type="password" placeholder="********" class="w-full bg-slate-100 border border-slate-200 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-brand-gold">
                        </div>
                        <button onclick="submitLogin()" class="w-full bg-brand-deep hover:bg-brand-mid text-white py-3 rounded-xl font-bold text-sm shadow transition">تسجيل الدخول</button>
                    </div>
                `;
            } else {
                signupBtn.className = "flex-1 pb-2 font-bold text-brand-deep border-b-2 border-brand-deep text-sm";
                loginBtn.className = "flex-1 pb-2 font-bold text-slate-400 text-sm";
                container.innerHTML = `
                    <div class="space-y-4">
                        <div>
                            <label class="block text-xs font-bold text-slate-700 mb-1">الاسم الكامل</label>
                            <input type="text" placeholder="اسمك الكريم" class="w-full bg-slate-100 border border-slate-200 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-brand-gold">
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-slate-700 mb-1">رقم الهاتف</label>
                            <input type="text" placeholder="010xxxxxxxx" class="w-full bg-slate-100 border border-slate-200 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-brand-gold">
                        </div>
                        <button onclick="submitSignup()" class="w-full bg-brand-deep hover:bg-brand-mid text-white py-3 rounded-xl font-bold text-sm shadow transition">إنشاء الحساب</button>
                    </div>
                `;
            }
        }

        function submitLogin() {
            alert('تم تسجيل الدخول بنجاح.');
            closeAuthModal();
        }

        function submitSignup() {
            alert('تم إنشاء الحساب بنجاح.');
            closeAuthModal();
        }

        function socialAuth(provider) {
            alert(`التسجيل عبر ${provider} متاح قريباً.`);
        }

        // Merchant Management Functions
        function getMerchantProfile(shopName) {
            const saved = localStorage.getItem(`merchant_${shopName}`);
            if (saved) {
                try { return JSON.parse(decodeURIComponent(atob(saved))); } catch(e) {}
            }
            return { phone: '01118872502', verified: true };
        }

        function saveMerchantProfile(shopName, profile) {
            saveSecureData(`merchant_${shopName}`, profile);
        }

        function openMerchantPanel() {
            document.getElementById('merchant-login-modal').classList.remove('hidden');
        }

        function closeMerchantLoginModal() {
            document.getElementById('merchant-login-modal').classList.add('hidden');
        }

        function submitMerchantLogin() {
            const phoneInput = document.getElementById('merchant-whatsapp-input').value.trim();
            const profile = getMerchantProfile(currentShopName);
            
            if (phoneInput === profile.phone || phoneInput === '01118872502') {
                merchantEditMode = true;
                closeMerchantLoginModal();
                showMerchantDashboard(profile);
                alert('تم التحقق بنجاح! تم تفعيل وضع تعديل وإدارة المتجر.');
            } else {
                alert('رقم الواتساب غير صحيح للمتجر.');
            }
        }

        function showMerchantDashboard(profile) {
            toggleMerchantEditControls(true);
        }

        function toggleMerchantEditControls(enable) {
            const controls = document.querySelectorAll('.merchant-edit-ctrl');
            controls.forEach(el => {
                if (enable) {
                    el.classList.remove('hidden');
                    el.classList.add('flex');
                } else {
                    el.classList.add('hidden');
                    el.classList.remove('flex');
                }
            });
        }

        // Information Modal Functions
        function openInfoModal(key) {
            const info = infoContent[key];
            if (!info) return;
            document.getElementById('info-modal-title').innerText = info.title;
            document.getElementById('info-modal-body').innerText = info.text;
            document.getElementById('info-modal').classList.remove('hidden');
        }

        function closeInfoModal() {
            document.getElementById('info-modal').classList.add('hidden');
        }

        // Shipping Companies Functions
        function renderShippingCompanies() {
            const grid = document.getElementById('shipping-grid');
            if (!grid) return;
            let html = '';
            shippingCompanies.forEach(comp => {
                html += `
                    <div class="bg-white p-5 rounded-2xl text-center shadow-sm border border-slate-200 flex flex-col items-center justify-center gap-2">
                        <div class="w-10 h-10 bg-brand-deep/10 text-brand-deep rounded-xl flex items-center justify-center text-lg"><i class="fa-solid ${comp.icon}"></i></div>
                        <span class="font-bold text-xs text-slate-800">${comp.name}</span>
                    </div>
                `;
            });
            grid.innerHTML = html;
        }

        // Shop Data Management Functions
        function buildDefaultShopData() {
            let shelves = [];
            for (let i = 1; i <= 10; i++) {
                shelves.push({ id: i, name: i <= 2 ? `قسم العروض الكبرى ${i}` : `رف منتجات رقم ${i}`, desc: 'أفضل السلع والمنتجات عالية الجودة' });
            }
            let products = [];
            for (let i = 1; i <= 10; i++) {
                products.push({ id: i, name: `منتج مميز رقم ${i}`, price: i <= 5 ? '120 جنيه' : '250 جنيه', discount: i <= 5 });
            }
            return { shelves, products, logo: '', cover: '', bio: 'متجر معتمد داخل محافظة السويس، نقدم أفضل المنتجات والخدمات لعملائنا.' };
        }

        function getShopData(shopName) {
            if (shopDataCache[shopName]) return shopDataCache[shopName];
            const saved = localStorage.getItem(`shopdata_${shopName}`);
            if (saved) {
                try {
                    shopDataCache[shopName] = JSON.parse(decodeURIComponent(atob(saved)));
                    return shopDataCache[shopName];
                } catch(e) {}
            }
            shopDataCache[shopName] = buildDefaultShopData();
            return shopDataCache[shopName];
        }

        function saveShopData(shopName) {
            saveSecureData(`shopdata_${shopName}`, shopDataCache[shopName]);
        }

        function renderShelvesForShop(shopName) {
            const data = getShopData(shopName);
            const grid = document.getElementById('shelves-grid');
            if (!grid) return;
            let html = '';
            data.shelves.forEach(shelf => {
                html += `
                    <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm flex flex-col justify-between relative">
                        <div>
                            <div class="flex justify-between items-start mb-2">
                                <h4 class="font-bold text-slate-900 text-base">${shelf.name}</h4>
                                <div class="hidden merchant-edit-ctrl gap-1">
                                    <button onclick="editShelf('${shopName}', ${shelf.id})" class="text-xs bg-slate-100 hover:bg-slate-200 p-1.5 rounded-lg text-slate-700" title="تعديل"><i class="fa-solid fa-pen"></i></button>
                                    <button onclick="deleteShelf('${shopName}', ${shelf.id})" class="text-xs bg-rose-50 hover:bg-rose-100 p-1.5 rounded-lg text-rose-600" title="حذف"><i class="fa-solid fa-trash"></i></button>
                                </div>
                            </div>
                            <p class="text-xs text-slate-500 mb-4">${shelf.desc}</p>
                        </div>
                        <span class="text-xs font-bold text-emerald-600 flex items-center gap-1"><i class="fa-brands fa-whatsapp"></i> استفسر عن الرف بالواتساب</span>
                    </div>
                `;
            });
            grid.innerHTML = html;
        }

        function editShelf(shopName, id) {
            const data = getShopData(shopName);
            const shelf = data.shelves.find(s => s.id === id);
            if (!shelf) return;
            const newName = prompt("أدخل اسم الرف الجديد:", shelf.name);
            if (newName) {
                shelf.name = newName;
                saveShopData(shopName);
                renderShelvesForShop(shopName);
            }
        }

        function deleteShelf(shopName, id) {
            const data = getShopData(shopName);
            data.shelves = data.shelves.filter(s => s.id !== id);
            saveShopData(shopName);
            renderShelvesForShop(shopName);
        }

        function addShelf() {
            const data = getShopData(currentShopName);
            const name = prompt("اسم الرف الجديد:");
            if (name) {
                data.shelves.push({ id: Date.now(), name: name, desc: 'قسم جديد مضاف' });
                saveShopData(currentShopName);
                renderShelvesForShop(currentShopName);
            }
        }

        function renderProductsForShop(shopName) {
            const data = getShopData(shopName);
            const grid = document.getElementById('products-grid');
            if (!grid) return;
            let html = '';
            data.products.forEach(prod => {
                html += `
                    <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex flex-col justify-between">
                        <div>
                            <div class="w-full h-32 bg-slate-100 rounded-xl mb-3 flex items-center justify-center text-slate-400 relative">
                                <i class="fa-solid fa-box text-3xl"></i>
                                ${prod.discount ? '<span class="absolute top-2 right-2 bg-brand-gold text-brand-deep text-[10px] font-bold px-2 py-0.5 rounded-full">خصم خاص</span>' : ''}
                            </div>
                            <h5 class="font-bold text-slate-800 text-sm mb-1">${prod.name}</h5>
                            <p class="text-xs font-black text-brand-deep mb-3">${prod.price}</p>
                        </div>
                        <a href="https://wa.me/201118872502?text=أرغب في طلب ${prod.name} من ${shopName}" target="_blank" class="bg-emerald-600 hover:bg-emerald-500 text-white text-center py-2.5 rounded-xl text-xs font-bold flex items-center justify-center gap-1">
                            <i class="fa-brands fa-whatsapp text-sm"></i> اطلب الآن
                        </a>
                    </div>
                `;
            });
            grid.innerHTML = html;
        }

        function addProduct() {
            const data = getShopData(currentShopName);
            const name = prompt("اسم المنتج أو السلعة:");
            const price = prompt("السعر:");
            if (name && price) {
                data.products.push({ id: Date.now(), name, price, discount: false });
                saveShopData(currentShopName);
                renderProductsForShop(currentShopName);
            }
        }

        function changeLogoImage() {
            const url = prompt("أدخل رابط صورة الشعار الجديد:");
            if (url) {
                const data = getShopData(currentShopName);
                data.logo = url;
                saveShopData(currentShopName);
                applyShopBranding();
            }
        }

        function changeCoverImage() {
            const url = prompt("أدخل رابط صورة الغلاف الجديد:");
            if (url) {
                const data = getShopData(currentShopName);
                data.cover = url;
                saveShopData(currentShopName);
                applyShopBranding();
            }
        }

        function editShopBio() {
            const data = getShopData(currentShopName);
            const bio = prompt("أدخل النبذة التعريفية للمتجر:", data.bio);
            if (bio !== null) {
                data.bio = bio;
                saveShopData(currentShopName);
                renderShopBio();
            }
        }

        function renderShopBio() {
            const data = getShopData(currentShopName);
            const bioEl = document.getElementById('display-shop-bio');
            if (bioEl) bioEl.innerText = data.bio;
        }

        function applyShopBranding() {
            const data = getShopData(currentShopName);
            const logoEl = document.getElementById('shop-logo');
            const logoIcon = document.getElementById('shop-logo-icon');
            if (data.logo) {
                logoEl.style.backgroundImage = `url('${data.logo}')`;
                logoIcon.style.display = 'none';
            } else {
                logoEl.style.backgroundImage = 'none';
                logoIcon.style.display = 'block';
            }
            if (data.cover) {
                document.getElementById('shop-cover').style.backgroundImage = `url('${data.cover}')`;
            }
        }

        // Shop Rendering Functions (50 Shops)
        function renderShops() {
            const grid = document.getElementById('shops-grid');
            if (!grid) return;
            let html = '';
            for (let i = 1; i <= 50; i++) {
                const baseName = shopNames[(i - 1) % shopNames.length];
                const shopName = `${baseName} (${i})`;
                const catObj = cats[(i - 1) % cats.length];
                const rating = (4.0 + ((i % 7) * 0.1)).toFixed(1);

                html += `
                    <div onclick="openShop('${shopName}', '${catObj.name}')" class="card-hover bg-white p-5 rounded-2xl shadow-sm border border-slate-100 cursor-pointer flex flex-col justify-between">
                        <div>
                            <div class="w-full h-32 bg-slate-100 rounded-xl mb-4 flex items-center justify-center text-brand-deep text-3xl font-black relative overflow-hidden">
                                <i class="fa-solid fa-store"></i>
                                <span class="absolute top-2 left-2 bg-brand-gold text-brand-deep text-[11px] font-bold px-2 py-0.5 rounded-full"><i class="fa-solid fa-star text-[10px]"></i> ${rating}</span>
                            </div>
                            <h4 class="font-bold text-slate-900 text-base mb-1">${shopName}</h4>
                            <p class="text-[11px] text-brand-deep font-semibold mb-2">${catObj.name}</p>
                            <p class="text-xs text-slate-500 mb-4">${catObj.desc}</p>
                        </div>
                        <span class="text-xs font-bold text-emerald-600 flex items-center gap-1"><i class="fa-brands fa-whatsapp"></i> زيارة المتجر والطلب</span>
                    </div>
                `;
            }
            grid.innerHTML = html;
        }

        function renderCategories() {
            const grid = document.getElementById('categories-grid');
            if (!grid) return;
            let html = '';
            cats.forEach(cat => {
                html += `
                    <div onclick="secureAction('${cat.id}', () => { alert('تم تصفية النتائج للقسم: ${cat.name}'); })" class="card-hover bg-white p-6 rounded-2xl shadow-sm border border-slate-100 cursor-pointer flex items-center space-x-4 space-x-reverse group">
                        <div class="bg-brand-deep/10 text-brand-deep p-4 rounded-xl text-xl group-hover:bg-brand-deep group-hover:text-white transition"><i class="fa-solid ${cat.icon}"></i></div>
                        <div>
                            <h4 class="font-bold text-slate-800 text-lg">${cat.name}</h4>
                            <p class="text-xs text-slate-500 mt-1">${cat.desc}</p>
                        </div>
                    </div>
                `;
            });
            grid.innerHTML = html;
        }

        window.onload = function() {
            renderCategories();
            renderShippingCompanies();
            renderShops();
        };
    </script>
</body>
</html>