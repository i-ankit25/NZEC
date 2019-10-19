package com.kraken.blindssight;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import android.Manifest;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.speech.RecognizerIntent;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import java.util.Timer;
import java.util.TimerTask;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {
    private static final String TAG = "MainActivity";

    private Button searchBtn, locBtn, toggleBtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        searchBtn = findViewById(R.id.btn_search);
        locBtn = findViewById(R.id.btn_loc);
        toggleBtn = findViewById(R.id.btn_toggle);

        searchBtn.setOnClickListener(this);
        locBtn.setOnClickListener(this);
        toggleBtn.setOnClickListener(this);

        sendLoc();
    }

    @Override
    public void onClick(View view) {
        switch (view.getId()) {
            case R.id.btn_search:
                listenAndSearch();
                break;
            case R.id.btn_toggle:
                toggle();
                break;
        }
    }

    private void toggle() {
        // TODO: just hit this end-point
    }

    private void sendLoc() {
        new Timer().scheduleAtFixedRate(
                new TimerTask() {
                    @Override
                    public void run() {
                        if (ContextCompat.checkSelfPermission(MainActivity.this, Manifest.permission.ACCESS_FINE_LOCATION) == PackageManager.PERMISSION_GRANTED) {
                            LocationManager locationManager = (LocationManager) getSystemService(Context.LOCATION_SERVICE);
                            assert locationManager != null;
                            Location location = locationManager.getLastKnownLocation(LocationManager.GPS_PROVIDER);
                            Log.d(TAG, "sendLoc: lat: " + location.getLatitude() + ", lon: " + location.getLongitude());

                            // TODO: send to back end
//                            Toast.makeText(MainActivity.this, "lat: " + location.getLatitude() + ", lon: " + location.getLongitude(), Toast.LENGTH_SHORT).show();
                        }
                    }
                }, 0, 2000);
    }

    private void listenAndSearch() {
        Intent intent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);

        startActivityForResult(intent, 10);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == 10) {
            if (resultCode == RESULT_OK && data != null) {
                // TODO: send to backend
                Log.d(TAG, "onActivityResult: " + data.getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS).get(0));
            }
        }
    }
}
