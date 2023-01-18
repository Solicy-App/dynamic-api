# Handle API requests.
import json
from flask import request, jsonify

from api_exception import ValidationError
from modules import available_modules
from modules.__validator__ import validate


def direct_api(database):
    def __do_post() -> json:
        try:
            # API response that was received.
            api = request.json
            results = []

            for call in api['calls']:
                if call['name'] in list(available_modules.keys()):
                    print(f"Processing: '{call['name']}'.")

                    if available_modules[call['name']]['schema']:
                        validate(available_modules[call['name']]['schema'], call['args'])

                    result = available_modules[call['name']]['process'](db=database, args=call['args'])
                    results.append(result)
                else:
                    print(f"No processor class defined for '{api['calls'][call]['name']}'.")

            return jsonify([e.serialize() for e in results]), 200

        except ValidationError as error:
            return jsonify({'success': False, 'message': f"Validation Error: {error.message}"}), 400
        except Exception as e:
            return jsonify({'success': False, 'message': 'Unable to process submitted data.'}), 500

    return __do_post
