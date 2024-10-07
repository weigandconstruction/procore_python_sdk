# RestV10RfqsRfqIdResponsesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**contract_id** | **int** | Contract ID | 
**rfq_response** | [**RFQResponse1**](RFQResponse1.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_rfqs_rfq_id_responses_post_request import RestV10RfqsRfqIdResponsesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10RfqsRfqIdResponsesPostRequest from a JSON string
rest_v10_rfqs_rfq_id_responses_post_request_instance = RestV10RfqsRfqIdResponsesPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10RfqsRfqIdResponsesPostRequest.to_json())

# convert the object into a dict
rest_v10_rfqs_rfq_id_responses_post_request_dict = rest_v10_rfqs_rfq_id_responses_post_request_instance.to_dict()
# create an instance of RestV10RfqsRfqIdResponsesPostRequest from a dict
rest_v10_rfqs_rfq_id_responses_post_request_from_dict = RestV10RfqsRfqIdResponsesPostRequest.from_dict(rest_v10_rfqs_rfq_id_responses_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


