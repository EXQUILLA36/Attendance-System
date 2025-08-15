import React, { useEffect, useRef } from 'react';
import Quagga from '@ericblade/quagga2';

const BarcodeScanner = ({ onDetected }) => {
  const scannerRef = useRef(null);

  useEffect(() => {
    if (scannerRef.current) {
      Quagga.init({
        inputStream: {
          type: 'LiveStream',
          target: scannerRef.current,
          constraints: {
            facingMode: 'environment' // use rear camera on mobile
          },
        },
        decoder: {
          readers: ['code_128_reader', 'ean_reader', 'ean_8_reader', 'upc_reader'],
        },
      }, (err) => {
        if (err) {
          console.error('Error initializing Quagga:', err);
          return;
        }
        Quagga.start();
      });

      Quagga.onDetected(handleDetected);
    }

    // Clean up on unmount
    return () => {
      Quagga.offDetected(handleDetected);
      Quagga.stop();
    };
  }, []);

  const handleDetected = (result) => {
    const code = result.codeResult.code;
    if (onDetected) {
      onDetected(code);
    }
  };

  return (
    <div>
      <div
        ref={scannerRef}
        style={{
          width: '100%',
          maxWidth: '500px',
          height: '300px',
          margin: 'auto',
          borderRadius: '8px',
          overflow: 'hidden',
        }}
      />
    </div>
  );
};

export default BarcodeScanner;
