# ResponseLog

Response Log body

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | The Comments of the Response Log | [optional] 
**prostore_file_ids** | **List[int]** | An array of the Attachment IDs | [optional] 

## Example

```python
from procore_sdk.models.response_log import ResponseLog

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseLog from a JSON string
response_log_instance = ResponseLog.from_json(json)
# print the JSON string representation of the object
print(ResponseLog.to_json())

# convert the object into a dict
response_log_dict = response_log_instance.to_dict()
# create an instance of ResponseLog from a dict
response_log_from_dict = ResponseLog.from_dict(response_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


