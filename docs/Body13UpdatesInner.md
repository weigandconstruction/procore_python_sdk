# Body13UpdatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the Tax Code. REQUIRED if &#39;origin_id&#39; is not provided. | [optional] 
**code** | **str** | The Tax Code | [optional] 
**description** | **str** | The Description of the Tax Code | [optional] 
**origin_data** | **str** | Additional Third-party Metadata for the Tax Code. Note: This is a free-form text field. | [optional] 
**origin_id** | **str** | The Third-party ID of the Tax Code. REQUIRED on update if &#39;id&#39; is not provided. | [optional] 
**rate1** | **float** | Rate to apply for first Tax Type | [optional] 
**archived** | **bool** | Set to true if this tax code has been archived | [optional] 

## Example

```python
from procore_sdk.models.body13_updates_inner import Body13UpdatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of Body13UpdatesInner from a JSON string
body13_updates_inner_instance = Body13UpdatesInner.from_json(json)
# print the JSON string representation of the object
print(Body13UpdatesInner.to_json())

# convert the object into a dict
body13_updates_inner_dict = body13_updates_inner_instance.to_dict()
# create an instance of Body13UpdatesInner from a dict
body13_updates_inner_from_dict = Body13UpdatesInner.from_dict(body13_updates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


