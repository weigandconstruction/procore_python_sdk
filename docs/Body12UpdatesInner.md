# Body12UpdatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the Tax Type. REQUIRED if &#39;origin_id&#39; is not provided. | [optional] 
**description** | **str** | The Description of the Tax Type | [optional] 
**name** | **str** | The Name of the Tax Type | [optional] 
**origin_data** | **str** | Additional Third-party Metadata for the Tax Type. Note: This is a free-form text field. | [optional] 
**origin_id** | **str** | The Third-party ID of the Tax Type. REQUIRED on update if &#39;id&#39; is not provided. | [optional] 

## Example

```python
from procore_sdk.models.body12_updates_inner import Body12UpdatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of Body12UpdatesInner from a JSON string
body12_updates_inner_instance = Body12UpdatesInner.from_json(json)
# print the JSON string representation of the object
print(Body12UpdatesInner.to_json())

# convert the object into a dict
body12_updates_inner_dict = body12_updates_inner_instance.to_dict()
# create an instance of Body12UpdatesInner from a dict
body12_updates_inner_from_dict = Body12UpdatesInner.from_dict(body12_updates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


