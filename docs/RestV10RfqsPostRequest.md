# RestV10RfqsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**contract_id** | **int** | Contract ID | 
**rfq** | [**RFQ1**](RFQ1.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_rfqs_post_request import RestV10RfqsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10RfqsPostRequest from a JSON string
rest_v10_rfqs_post_request_instance = RestV10RfqsPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10RfqsPostRequest.to_json())

# convert the object into a dict
rest_v10_rfqs_post_request_dict = rest_v10_rfqs_post_request_instance.to_dict()
# create an instance of RestV10RfqsPostRequest from a dict
rest_v10_rfqs_post_request_from_dict = RestV10RfqsPostRequest.from_dict(rest_v10_rfqs_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


