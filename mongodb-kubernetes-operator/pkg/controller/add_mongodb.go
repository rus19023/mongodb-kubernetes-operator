package controller

import (
	"github.com/mongodb/mongodb-kubernetes-operator/mongodb-kubernetes-operator/pkg/controller/mongodb"
)

func init() {
	// AddToManagerFuncs is a list of functions to create controllers and add them to a manager.
	AddToManagerFuncs = append(AddToManagerFuncs, mongodb.Add)
}
