# Body44


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**attachments** | **List[str]** | Prime Contract attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 
**prime_contract** | [**PrimeContract**](PrimeContract.md) |  | 

## Example

```python
from procore_sdk.models.body44 import Body44

# TODO update the JSON string below
json = "{}"
# create an instance of Body44 from a JSON string
body44_instance = Body44.from_json(json)
# print the JSON string representation of the object
print(Body44.to_json())

# convert the object into a dict
body44_dict = body44_instance.to_dict()
# create an instance of Body44 from a dict
body44_from_dict = Body44.from_dict(body44_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


