# Body13


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID | 
**updates** | [**List[Body13UpdatesInner]**](Body13UpdatesInner.md) |  | 

## Example

```python
from procore_sdk.models.body13 import Body13

# TODO update the JSON string below
json = "{}"
# create an instance of Body13 from a JSON string
body13_instance = Body13.from_json(json)
# print the JSON string representation of the object
print(Body13.to_json())

# convert the object into a dict
body13_dict = body13_instance.to_dict()
# create an instance of Body13 from a dict
body13_from_dict = Body13.from_dict(body13_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


