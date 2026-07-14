import streamlit as st
import pandas as pd

# Sayfa ayarları
st.set_page_config(page_title="SASL-300 Program Seçici", layout="centered")

# Veri seti
data = [
    {"ProgramNo": 0, "Cap": 25.0, "EtKalinligi": 2.0, "KaynakModel": "SATP-80", "Mode": "KAYNAK", "KaynakTipi": "DANONDE"},
    {"ProgramNo": 1, "Cap": 15.0, "EtKalinligi": 1.5, "KaynakModel": "SATP-80", "Mode": "KAYNAK+TEL", "KaynakTipi": "YOK"},
    {"ProgramNo": 2, "Cap": 18.0, "EtKalinligi": 1.5, "KaynakModel": "SATP-80", "Mode": "KAYNAK", "KaynakTipi": "TUBULER"},
    {"ProgramNo": 3, "Cap": 18.0, "EtKalinligi": 1.0, "KaynakModel": "SATP-80", "Mode": "KAYNAK", "KaynakTipi": "BORU+FLANŞ"},
    {"ProgramNo": 4, "Cap": 15.0, "EtKalinligi": 1.5, "KaynakModel": "SATP-80", "Mode": "KAYNAK", "KaynakTipi": "BORU+BORU"},
    {"ProgramNo": 5, "Cap": 85.0, "EtKalinligi": 2.0, "KaynakModel": "SC171E", "Mode": "KAYNAK", "KaynakTipi": "BORU+FITTINGS"},
    {"ProgramNo": 6, "Cap": 53.0, "EtKalinligi": 1.5, "KaynakModel": "SC170E", "Mode": "KAYNAK", "KaynakTipi": "REDÜKSİYON+FITTINGS"},
    {"ProgramNo": 7, "Cap": 41.0, "EtKalinligi": 1.5, "KaynakModel": "SC170E", "Mode": "KAYNAK", "KaynakTipi": "BORU+FITTINGS"},
    {"ProgramNo": 8, "Cap": 85.0, "EtKalinligi": 2.0, "KaynakModel": "SC170E", "Mode": "KAYNAK", "KaynakTipi": "BORU+FITTINGS"},
    {"ProgramNo": 9, "Cap": 104.0, "EtKalinligi": 2.0, "KaynakModel": "SC170E", "Mode": "KAYNAK", "KaynakTipi": "BORU+FITTINGS"},
    {"ProgramNo": 10, "Cap": 104.0, "EtKalinligi": 2.0, "KaynakModel": "SC170E", "Mode": "KAYNAK", "KaynakTipi": "BORU+DİRSEK"},
    {"ProgramNo": 11, "Cap": 85.0, "EtKalinligi": 2.0, "KaynakModel": "SC170E", "Mode": "KAYNAK", "KaynakTipi": "BORU+FITTINGS"},
    {"ProgramNo": 12, "Cap": 16.0, "EtKalinligi": 2.0, "KaynakModel": "SATP-80", "Mode": "KAYNAK", "KaynakTipi": "YOK"},
    {"ProgramNo": 13, "Cap": 104.0, "EtKalinligi": 2.0, "KaynakModel": "SC170E", "Mode": "KAYNAK", "KaynakTipi": "BORU+BORU"},
    {"ProgramNo": 14, "Cap": 53.0, "EtKalinligi": 1.5, "KaynakModel": "SATP-80", "Mode": "KAYNAK", "KaynakTipi": "BORU+FLANŞ"},
    {"ProgramNo": 15, "Cap": 41.0, "EtKalinligi": 1.5, "KaynakModel": "SATP-80", "Mode": "KAYNAK", "KaynakTipi": "BORU+FLANŞ"},
    {"ProgramNo": 16, "Cap": 70.0, "EtKalinligi": 2.0, "KaynakModel": "SATP-80", "Mode": "KAYNAK", "KaynakTipi": "BORU+FLANŞ"},
    {"ProgramNo": 17, "Cap": 29.0, "EtKalinligi": 1.5, "KaynakModel": "SC170E", "Mode": "KAYNAK", "KaynakTipi": "BORU+FITTINGS"},
    {"ProgramNo": 18, "Cap": 41.0, "EtKalinligi": 1.5, "KaynakModel": "SC170E", "Mode": "KAYNAK", "KaynakTipi": "BORU+FITTINGS"},
    {"ProgramNo": 19, "Cap": 85.0, "EtKalinligi": 2.0, "KaynakModel": "SC170A", "Mode": "KAYNAK", "KaynakTipi": "BORU+BORU"},
    {"ProgramNo": 20, "Cap": 85.0, "EtKalinligi": 2.0, "KaynakModel": "SC170A", "Mode": "PUNTA", "KaynakTipi": "BORU+BORU"},
    {"ProgramNo": 21, "Cap": 85.0, "EtKalinligi": 2.0, "KaynakModel": "SC170E", "Mode": "KAYNAK", "KaynakTipi": "BORU+BORU"},
    {"ProgramNo": 22, "Cap": 85.0, "EtKalinligi": 2.0, "KaynakModel": "SC171A", "Mode": "KAYNAK", "KaynakTipi": "BORU+BORU"},
    {"ProgramNo": 23, "Cap": 85.0, "EtKalinligi": 2.0, "KaynakModel": "SC170A", "Mode": "KAYNAK", "KaynakTipi": "BORU+BORU"},
    {"ProgramNo": 24, "Cap": 70.0, "EtKalinligi": 2.0, "KaynakModel": "SC170E", "Mode": "PUNTA", "KaynakTipi": "BORU+BORU"},
    {"ProgramNo": 25, "Cap": 70.0, "EtKalinligi": 2.0, "KaynakModel": "SC170E", "Mode": "KAYNAK", "KaynakTipi": "BORU+BORU"},
    {"ProgramNo": 26, "Cap": 85.0, "EtKalinligi": 2.0, "KaynakModel": "SC170E", "Mode": "KAYNAK", "KaynakTipi": "REDÜKSİYON+FITTINGS"},
    {"ProgramNo": 27, "Cap": 85.0, "EtKalinligi": 2.0, "KaynakModel": "SC170E", "Mode": "KAYNAK", "KaynakTipi": "BORU+BORU"},
    {"ProgramNo": 28, "Cap": 139.7, "EtKalinligi": 4.0, "KaynakModel": "SC170E", "Mode": "KAYNAK", "KaynakTipi": "REDÜKSİYON+FITTINGS"},
    {"ProgramNo": 29, "Cap": 129.0, "EtKalinligi": 2.0, "KaynakModel": "SC170E", "Mode": "KAYNAK", "KaynakTipi": "BORU+BORU"},
    {"ProgramNo": 30, "Cap": 85.0, "EtKalinligi": 2.0, "KaynakModel": "SC171E", "Mode": "KAYNAK", "KaynakTipi": "BORU+BORU"},
    {"ProgramNo": 31, "Cap": 70.0, "EtKalinligi": 2.0, "KaynakModel": "SATF-115ND", "Mode": "KAYNAK", "KaynakTipi": "BORU+BORU"},
    {"ProgramNo": 32, "Cap": 70.0, "EtKalinligi": 2.0, "KaynakModel": "SC170E", "Mode": "KAYNAK", "KaynakTipi": "FITTINGS+FITTINGS"},
    {"ProgramNo": 33, "Cap": 70.0, "EtKalinligi": 2.0, "KaynakModel": "SC170E", "Mode": "KAYNAK", "KaynakTipi": "BORU+FITTINGS"},
    {"ProgramNo": 34, "Cap": 85.0, "EtKalinligi": 2.0, "KaynakModel": "SATF-115ND", "Mode": "KAYNAK", "KaynakTipi": "BORU+DİRSEK"},
    {"ProgramNo": 35, "Cap": 104.0, "EtKalinligi": 2.0, "KaynakModel": "SATF-115ND", "Mode": "KAYNAK", "KaynakTipi": "BORU+DİRSEK"},
    {"ProgramNo": 36, "Cap": 53.0, "EtKalinligi": 1.5, "KaynakModel": "SC170E", "Mode": "KAYNAK", "KaynakTipi": "BORU+BORU"},
    {"ProgramNo": 37, "Cap": 53.0, "EtKalinligi": 1.5, "KaynakModel": "SC170E", "Mode": "PUNTA", "KaynakTipi": "YOK"},
    {"ProgramNo": 38, "Cap": 29.0, "EtKalinligi": 1.5, "KaynakModel": "SC170A", "Mode": "KAYNAK", "KaynakTipi": "BORU+FITTINGS"},
    {"ProgramNo": 39, "Cap": 28.0, "EtKalinligi": 1.5, "KaynakModel": "SC170E", "Mode": "KAYNAK", "KaynakTipi": "FITTINGS+FITTINGS"},
    {"ProgramNo": 40, "Cap": 16.0, "EtKalinligi": 1.0, "KaynakModel": "SATP-80", "Mode": "KAYNAK", "KaynakTipi": "BORU+BORU"},
    {"ProgramNo": 43, "Cap": 33.7, "EtKalinligi": 2.0, "KaynakModel": "SC170E", "Mode": "KAYNAK", "KaynakTipi": "BORU+FITTINGS"},
    {"ProgramNo": 50, "Cap": 139.7, "EtKalinligi": 2.0, "KaynakModel": "SC170E", "Mode": "KAYNAK", "KaynakTipi": "BORU+FLANŞ"},
    {"ProgramNo": 60, "Cap": 70.0, "EtKalinligi": 1.5, "KaynakModel": "SC171A", "Mode": "KAYNAK", "KaynakTipi": "BORU+BORU"},
    {"ProgramNo": 61, "Cap": 53.0, "EtKalinligi": 1.5, "KaynakModel": "SC171A", "Mode": "KAYNAK", "KaynakTipi": "BORU+BORU"},
    {"ProgramNo": 70, "Cap": 18.0, "EtKalinligi": 1.5, "KaynakModel": "SATP-80", "Mode": "KAYNAK+TEL", "KaynakTipi": "BORU+FLANŞ"},
    {"ProgramNo": 71, "Cap": 18.0, "EtKalinligi": 1.5, "KaynakModel": "SATP-80", "Mode": "KAYNAK", "KaynakTipi": "BORU+FLANŞ"},
    {"ProgramNo": 72, "Cap": 53.0, "EtKalinligi": 2.0, "KaynakModel": "SATP-80", "Mode": "KAYNAK", "KaynakTipi": "BORU+BORU"}
    
]

# Veriyi Pandas DataFrame'e çevirme
df = pd.DataFrame(data)
df_filtered = df.copy() # Filtreleme yapacağımız kopya tablo

# --- ARAYÜZ TASARIMI ---
st.title("🔧 SASL-300 Program Seçici")
st.markdown("Kriterleri sırasıyla seçin. Seçim yaptıkça aşağıdaki liste otomatik güncellenecektir.")
st.divider()

# Sütun yapısı kullanarak tasarımı daha kompakt hale getirelim (Yan yana kutular)
col1, col2 = st.columns(2)

with col1:
    # 1. ADIM: Kaynak Model Seçimi (Boş başlayacak)
    model_options = sorted(df_filtered['KaynakModel'].unique())
    model = st.selectbox("Kaynak Model:", model_options, index=None, placeholder="Tümü (Seçiniz)")
    if model: # Eğer bir model seçildiyse tabloyu daralt
        df_filtered = df_filtered[df_filtered['KaynakModel'] == model]

    # 3. ADIM: Mode Seçimi
    mode_options = sorted(df_filtered['Mode'].unique())
    mode = st.selectbox("Mode:", mode_options, index=None, placeholder="Tümü (Seçiniz)")
    if mode:
        df_filtered = df_filtered[df_filtered['Mode'] == mode]

    # 5. ADIM: Et Kalınlığı Seçimi
    et_options = sorted(df_filtered['EtKalinligi'].unique())
    et = st.selectbox("Et Kalınlığı (mm):", et_options, index=None, placeholder="Tümü (Seçiniz)")
    if et:
        df_filtered = df_filtered[df_filtered['EtKalinligi'] == et]

with col2:
    # 2. ADIM: Kaynak Tipi Seçimi
    tip_options = sorted(df_filtered['KaynakTipi'].unique())
    tip = st.selectbox("Kaynak Tipi:", tip_options, index=None, placeholder="Tümü (Seçiniz)")
    if tip:
        df_filtered = df_filtered[df_filtered['KaynakTipi'] == tip]

    # 4. ADIM: Çap Seçimi
    cap_options = sorted(df_filtered['Cap'].unique())
    cap = st.selectbox("Çap (mm):", cap_options, index=None, placeholder="Tümü (Seçiniz)")
    if cap:
        df_filtered = df_filtered[df_filtered['Cap'] == cap]

st.divider()

# --- CANLI TABLO GÖRÜNÜMÜ ---
st.subheader("📋 Uygun Program Listesi")

# Eğer filtrelemeler sonucunda hiç veri kalmadıysa uyarı ver
if df_filtered.empty:
    st.warning("❌ Bu kriterlere uygun bir program kaydı bulunamadı!")
else:
    # İnteraktif tabloyu ekrana yazdır (index numaralarını gizleyerek temiz görünüm sağladık)
    st.dataframe(df_filtered, use_container_width=True, hide_index=True)

    # Eğer seçimler listeyi tek bir programa kadar düşürdüyse dev bir başarı mesajı göster
    if len(df_filtered) == 1:
        bulunan_program = df_filtered.iloc[0]['ProgramNo']
        st.success(f"✅ KULLANILACAK PROGRAM NO: **{bulunan_program}**")
