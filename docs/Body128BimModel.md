# Body128BimModel

BIM Model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | BIM Model title | 
**auto_publish** | **bool** | Model auto publishing setting. When set to true, a new model revision is automatically published when a new version of the input model file is uploaded | [optional] 

## Example

```python
from procore_sdk.models.body128_bim_model import Body128BimModel

# TODO update the JSON string below
json = "{}"
# create an instance of Body128BimModel from a JSON string
body128_bim_model_instance = Body128BimModel.from_json(json)
# print the JSON string representation of the object
print(Body128BimModel.to_json())

# convert the object into a dict
body128_bim_model_dict = body128_bim_model_instance.to_dict()
# create an instance of Body128BimModel from a dict
body128_bim_model_from_dict = Body128BimModel.from_dict(body128_bim_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


