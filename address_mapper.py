
import streamlit as st
import folium
from geopy.geocoders import Nominatim
from streamlit_folium import st_folium

# Set up the Streamlit app
st.title("Address Mapper")
st.write("Enter one address per line and click 'Plot Addresses' to see them on the map.")

# Text area for address input
addresses_input = st.text_area("Addresses", height=200, placeholder="123 Main St, City, Country\n456 Another Rd, City, Country")

# Button to trigger plotting
if st.button("Plot Addresses"):
    if addresses_input.strip() == "":
        st.warning("Please enter at least one address.")
    else:
        # Initialize geocoder
        geolocator = Nominatim(user_agent="address_mapper")

        # Split addresses and initialize map
        addresses = addresses_input.strip().split("\n")
        map_center = [0, 0]
        map_obj = folium.Map(location=map_center, zoom_start=2)

        # Geocode and add markers
        for address in addresses:
            try:
                location = geolocator.geocode(address)
                if location:
                    folium.Marker(
                        [location.latitude, location.longitude],
                        popup=address,
                        tooltip=address
                    ).add_to(map_obj)
            except Exception as e:
                st.error(f"Error geocoding address '{address}': {e}")

        # Display map
        st_folium(map_obj, width=700, height=500)
