import { sleep, group, check } from 'k6'
import http from 'k6/http'

export const options = {
  ext: {
    loadimpact: {
      distribution: { 'amazon:se:stockholm': { loadZone: 'amazon:se:stockholm', percent: 100 } },
      apm: [],
    },
  },
  thresholds: { http_req_duration: ['p(90)<200'] },
  scenarios: {
    Scenario_1: {
      executor: 'constant-vus',
      gracefulStop: '30s',
      duration: '1m',
      vus: 1,
      exec: 'scenario_1',
    },
  },
}

export function scenario_1() {
  let response

  group('page_1 - https://betsspace.com/', function () {
    response = http.get('https://betsspace.com/', {
      headers: {
        'upgrade-insecure-requests': '1',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
      },
    })
    sleep(0.5)

    response = http.post(
      'https://betsspace.com/.well-known/shopify/monorail/unstable/produce_batch',
      null,
      {
        headers: {
          'content-type': 'text/plain',
          'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
        },
      }
    )

    response = http.post(
      'https://betsspace.com/.well-known/shopify/monorail/unstable/produce_batch',
      null,
      {
        headers: {
          'content-type': 'text/plain',
          'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
        },
      }
    )

    response = http.post(
      'https://betsspace.com/.well-known/shopify/monorail/unstable/produce_batch',
      null,
      {
        headers: {
          'content-type': 'text/plain',
          'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
        },
      }
    )

    response = http.post(
      'https://betsspace.com/.well-known/shopify/monorail/unstable/produce_batch',
      null,
      {
        headers: {
          'content-type': 'text/plain',
          'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
        },
      }
    )

    response = http.post(
      'https://betsspace.com/.well-known/shopify/monorail/unstable/produce_batch',
      '{"metadata":{"event_sent_at_ms":1669809728452},"events":[{"schema_id":"web_pixels_manager_load/2.0","payload":{"version":"0.0.177","page_url":"https://betsspace.com/","status":"loaded"},"metadata":{"event_created_at_ms":1669809728451}},{"schema_id":"web_pixels_manager_init/2.0","payload":{"version":"0.0.177","page_url":"https://betsspace.com/","shop_id":27083997299,"surface":"storefront-renderer","status":"initialized"},"metadata":{"event_created_at_ms":1669809728452}}]}',
      {
        headers: {
          'content-type': 'text/plain; charset=UTF-8',
          'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
        },
      }
    )

    response = http.post(
      'https://betsspace.com/.well-known/shopify/monorail/unstable/produce_batch',
      '{"metadata":{"event_sent_at_ms":1669809728454},"events":[{"schema_id":"web_pixels_manager_event_publish/1.0","payload":{"version":"0.0.177","page_url":"https://betsspace.com/","shop_id":27083997299,"surface":"storefront-renderer","event_name":"page_viewed","event_type":"standard"},"metadata":{"event_created_at_ms":1669809728454}}]}',
      {
        headers: {
          'content-type': 'text/plain; charset=UTF-8',
          'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
        },
      }
    )
    sleep(1.5)

    response = http.post('https://betsspace.com/.well-known/shopify/monorail/v1/produce', null, {
      headers: {
        'content-type': 'text/plain',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
      },
    })
    sleep(1.2)
  })

  group('page_2 - https://betsspace.com/collections/cushions', function () {
    response = http.get('https://betsspace.com/collections/cushions', {
      headers: {
        'upgrade-insecure-requests': '1',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
      },
    })
    sleep(1.1)

    response = http.post(
      'https://betsspace.com/.well-known/shopify/monorail/unstable/produce_batch',
      null,
      {
        headers: {
          'content-type': 'text/plain',
          'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
        },
      }
    )

    response = http.post(
      'https://betsspace.com/.well-known/shopify/monorail/unstable/produce_batch',
      '{"metadata":{"event_sent_at_ms":1669809732253},"events":[{"schema_id":"web_pixels_manager_load/2.0","payload":{"version":"0.0.177","page_url":"https://betsspace.com/collections/cushions","status":"loaded"},"metadata":{"event_created_at_ms":1669809732252}},{"schema_id":"web_pixels_manager_init/2.0","payload":{"version":"0.0.177","page_url":"https://betsspace.com/collections/cushions","shop_id":27083997299,"surface":"storefront-renderer","status":"initialized"},"metadata":{"event_created_at_ms":1669809732253}}]}',
      {
        headers: {
          'content-type': 'text/plain; charset=UTF-8',
          'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
        },
      }
    )

    response = http.post(
      'https://betsspace.com/.well-known/shopify/monorail/unstable/produce_batch',
      '{"metadata":{"event_sent_at_ms":1669809732254},"events":[{"schema_id":"web_pixels_manager_event_publish/1.0","payload":{"version":"0.0.177","page_url":"https://betsspace.com/collections/cushions","shop_id":27083997299,"surface":"storefront-renderer","event_name":"page_viewed","event_type":"standard"},"metadata":{"event_created_at_ms":1669809732254}}]}',
      {
        headers: {
          'content-type': 'text/plain; charset=UTF-8',
          'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
        },
      }
    )

    response = http.post(
      'https://betsspace.com/.well-known/shopify/monorail/unstable/produce_batch',
      '{"metadata":{"event_sent_at_ms":1669809732257},"events":[{"schema_id":"web_pixels_manager_event_publish/1.0","payload":{"version":"0.0.177","page_url":"https://betsspace.com/collections/cushions","shop_id":27083997299,"surface":"storefront-renderer","event_name":"collection_viewed","event_type":"standard"},"metadata":{"event_created_at_ms":1669809732257}}]}',
      {
        headers: {
          'content-type': 'text/plain; charset=UTF-8',
          'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
        },
      }
    )

    response = http.post(
      'https://betsspace.com/.well-known/shopify/monorail/unstable/produce_batch',
      null,
      {
        headers: {
          'content-type': 'text/plain',
          'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
        },
      }
    )

    response = http.post(
      'https://betsspace.com/.well-known/shopify/monorail/unstable/produce_batch',
      null,
      {
        headers: {
          'content-type': 'text/plain',
          'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
        },
      }
    )

    response = http.post(
      'https://betsspace.com/.well-known/shopify/monorail/unstable/produce_batch',
      null,
      {
        headers: {
          'content-type': 'text/plain',
          'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
        },
      }
    )

    response = http.post(
      'https://betsspace.com/.well-known/shopify/monorail/unstable/produce_batch',
      null,
      {
        headers: {
          'content-type': 'text/plain',
          'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
        },
      }
    )
    sleep(1.4)
  })

  group('page_3 - https://betsspace.com/collections/cushions/products/joseph-cush', function () {
    response = http.get('https://betsspace.com/collections/cushions/products/joseph-cush', {
      headers: {
        'upgrade-insecure-requests': '1',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
      },
    })

    response = http.post('https://betsspace.com/.well-known/shopify/monorail/v1/produce', null, {
      headers: {
        'content-type': 'text/plain',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
      },
    })
    sleep(0.6)

    response = http.post(
      'https://betsspace.com/.well-known/shopify/monorail/unstable/produce_batch',
      null,
      {
        headers: {
          'content-type': 'text/plain',
          'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
        },
      }
    )

    response = http.post(
      'https://betsspace.com/.well-known/shopify/monorail/unstable/produce_batch',
      null,
      {
        headers: {
          'content-type': 'text/plain',
          'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
        },
      }
    )

    response = http.post(
      'https://betsspace.com/.well-known/shopify/monorail/unstable/produce_batch',
      null,
      {
        headers: {
          'content-type': 'text/plain',
          'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
        },
      }
    )

    response = http.post(
      'https://betsspace.com/.well-known/shopify/monorail/unstable/produce_batch',
      null,
      {
        headers: {
          'content-type': 'text/plain',
          'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
        },
      }
    )

    response = http.post(
      'https://betsspace.com/.well-known/shopify/monorail/unstable/produce_batch',
      null,
      {
        headers: {
          'content-type': 'text/plain',
          'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
        },
      }
    )

    response = http.post(
      'https://betsspace.com/.well-known/shopify/monorail/unstable/produce_batch',
      null,
      {
        headers: {
          'content-type': 'text/plain',
          'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
        },
      }
    )

    response = http.post(
      'https://betsspace.com/.well-known/shopify/monorail/unstable/produce_batch',
      '{"metadata":{"event_sent_at_ms":1669809734756},"events":[{"schema_id":"web_pixels_manager_load/2.0","payload":{"version":"0.0.177","page_url":"https://betsspace.com/collections/cushions/products/joseph-cush","status":"loaded"},"metadata":{"event_created_at_ms":1669809734756}},{"schema_id":"web_pixels_manager_init/2.0","payload":{"version":"0.0.177","page_url":"https://betsspace.com/collections/cushions/products/joseph-cush","shop_id":27083997299,"surface":"storefront-renderer","status":"initialized"},"metadata":{"event_created_at_ms":1669809734756}}]}',
      {
        headers: {
          'content-type': 'text/plain; charset=UTF-8',
          'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
        },
      }
    )

    response = http.post(
      'https://betsspace.com/.well-known/shopify/monorail/unstable/produce_batch',
      '{"metadata":{"event_sent_at_ms":1669809734757},"events":[{"schema_id":"web_pixels_manager_event_publish/1.0","payload":{"version":"0.0.177","page_url":"https://betsspace.com/collections/cushions/products/joseph-cush","shop_id":27083997299,"surface":"storefront-renderer","event_name":"page_viewed","event_type":"standard"},"metadata":{"event_created_at_ms":1669809734757}}]}',
      {
        headers: {
          'content-type': 'text/plain; charset=UTF-8',
          'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
        },
      }
    )

    response = http.post(
      'https://betsspace.com/.well-known/shopify/monorail/unstable/produce_batch',
      '{"metadata":{"event_sent_at_ms":1669809734758},"events":[{"schema_id":"web_pixels_manager_event_publish/1.0","payload":{"version":"0.0.177","page_url":"https://betsspace.com/collections/cushions/products/joseph-cush","shop_id":27083997299,"surface":"storefront-renderer","event_name":"product_viewed","event_type":"standard"},"metadata":{"event_created_at_ms":1669809734758}}]}',
      {
        headers: {
          'content-type': 'text/plain; charset=UTF-8',
          'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
        },
      }
    )

    response = http.get(
      'https://betsspace.com/recommendations/products?section_id=product-recommendations&product_id=6866716590279&limit=4',
      {
        headers: {
          accept: '*/*',
          'x-requested-with': 'XMLHttpRequest',
          'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
        },
      }
    )

    response = http.get('https://betsspace.com/payments/config?currency=SEK', {
      headers: {
        accept: 'application/json',
        'content-type': 'application/json',
        'x-shopify-wallets-caller': 'costanza',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-shopify-api-version': '2018-02-15',
      },
    })
    sleep(1)

    response = http.post(
      'https://betsspace.com/api/graphql',
      '{\n  shop {\n    paymentSettings {\n      currencyCode\n    }\n  }\n  node(id: "Z2lkOi8vc2hvcGlmeS9Qcm9kdWN0VmFyaWFudC80MDQ4Mzg0NDk4MDkzNQ==") {\n    ... on ProductVariant {\n      requiresShipping\n      price\n      presentmentPrices(first: 25) {\n        edges {\n          node {\n            price {\n              amount\n              currencyCode\n            }\n          }\n        }\n      }\n    }\n  }\n}',
      {
        headers: {
          'content-type': 'application/graphql',
          'x-shopify-storefront-access-token': 'f5cc5f3c699f99db0da343fef1d27bda',
          'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
        },
      }
    )

    response = http.post('https://betsspace.com/.well-known/shopify/monorail/v1/produce', null, {
      headers: {
        'content-type': 'text/plain',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
      },
    })
    sleep(0.5)

    response = http.post(
      'https://betsspace.com/cart/update.js',
      '{"updates":{"40483844980935":2}}',
      {
        headers: {
          accept: 'application/json, text/plain, */*',
          'content-type': 'application/json; charset=UTF-8',
          'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
        },
      }
    )
  })
}
